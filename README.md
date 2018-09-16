# Knickretreat
Simple code to calculate knickpoint retreat through a catchment dependent on upstream drainage area and lithological strength

# Requirements
This code is written in Python 2

# Usage
1. extract your long profile using your preferred method and software, calculating downstream distance, drainage area, and DEM elevation
2. format a csv file with columns Downstream distance; Drainage Area, DEM height, Erosional efficiency.
3. run this code

Output is the position of the knickpoint calculated using your chosen age and erosional efficiency. This is compared against the observed knickpoint. Average modelled retreat rate is also reported.
Two graphs plot (1) the position of the knickpoint downstream over time; (2) the retreat rate of the knickpoint through time.
