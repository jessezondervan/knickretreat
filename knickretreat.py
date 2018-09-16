#choose a value for precipitation in m/yr:
p = 

#choose upstream distance of the knickpoint (m) and the time of intiation (yr):
knick = 
knickage = 

#open your csv file with the formatted columns occurding to the readme instructions:
#remember to have a column with downstream distance (not upstream distance)
fil = open('C:/Users/jzondervan/Code/knickpoint_retreat.csv')

#channel width to drainage area scaling (optional, default) (dimensionless):
w2a = 0.001

#Output is the position of the knickpoint calculated using your chosen age and erosional efficiency.
#This is compared against the observed knickpoint.
#Average modelled retreat rate is also reported.
#Two graphs plot: 
#(1) the position of the knickpoint downstream over time;
#(2) the retreat rate of the knickpoint through time.

####################################################################################################
# Function written by Jesse R. Zondervan - Updated : 16/09/18
####################################################################################################

Downstream_dist = []
Area = []
Elev = []
Eff = []

for line in fil:
    Downstream_dist.append(float(line.split(',')[0]))
    Area.append(float(line.split(',')[1]))
    Elev.append(float(line.split(',')[2]))
    Eff.append(float(line.split(',')[3]))

import numpy as np

Lf = max(Downstream_dist) # m
Lk = max(Downstream_dist) # m
Psi = 10*1000*p*w2a # 

endLk = max(Downstream_dist) - knick # m

t=0
ht = 10000 # yr

posLk = min(Downstream_dist, key=lambda x:abs(x-endLk))
lowerLk = min(Downstream_dist, key=lambda x:abs(x-Lf))
posLf = min(Downstream_dist, key=lambda x:abs(x-Lf))
print 'first estimate of the age of knickpoint %.f yrs' % knickage

vlist = [0]
Lk_lst = [Lk]
t_lst = [t]

for i in range(int(knickage/ht)):
    dclose = min(Downstream_dist, key=lambda x:abs(x-Lk))
    if dclose - Lk <0:
        A = ((Area[Downstream_dist.index(dclose)+1]-Area[Downstream_dist.index(dclose)])/
        (Downstream_dist[Downstream_dist.index(dclose)+1]-dclose))*(Lk-dclose)+Area[Downstream_dist.index(dclose)]
    else:
        A = ((Area[Downstream_dist.index(dclose)]-Area[Downstream_dist.index(dclose)-1])/
        (dclose-Downstream_dist[Downstream_dist.index(dclose)-1]))*(Lk-Downstream_dist[Downstream_dist.index(dclose)-1])+Area[Downstream_dist.index(dclose)-1]
    Ef = Eff[Downstream_dist.index(dclose)]
    
    v = Psi*Ef*365*3600*24*np.sqrt(A)*1000 # mm/yr
    vlist.append(v)
    Lk = Lk - v*ht/1000
    Lk_lst.append(Lk)
    t = t+ht
    t_lst.append(t)

import matplotlib.pyplot as plt
%matplotlib inline
plt.plot(t_lst, Lk_lst)
plt.show()

plt.plot(t_lst, vlist)
plt.show()    

print 'observed knickpoint at %.f m downstream and %.f m elevation' % (endLk, Elev[Downstream_dist.index(posLk)])
print 'knickpoint position calculated by function = %.f' % Lk
print 'Average retreat rate is %.f mm/yr' % (np.mean(vlist))
