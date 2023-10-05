import csv
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#from matplotlib.mpl_toolkits.mplot3d.axes3d import Axes3D 

rownum = 0

latitude = []
longitude = []
elevation = []

heightfile = open("NASA_app/files/LeibnitzBetaPlateau/FY23_ADC_Height_LeibnitzBetaPlateau.csv",'r')

for row in csv.reader(heightfile):      #Read pairs file row by row
    if (rownum < 20):
        elevation.append(float(row[0]))
    rownum = rownum + 1
rownum=0
lonfile = open("NASA_app/files/LeibnitzBetaPlateau/FY23_ADC_Longitude_LeibnitzBetaPlateau.csv",'r') 

for row in csv.reader(lonfile):      #Read pairs file row by row
    if (rownum <20): 
        longitude.append(float(row[0]))            
    rownum = rownum + 1
rownum=0
latfile = open("NASA_app/files/LeibnitzBetaPlateau/FY23_ADC_Latitude_LeibnitzBetaPlateau.csv",'r')

for row in csv.reader(latfile):      #Read pairs file row by row 
    if (rownum <20): 
        latitude.append(float(row[0]))             
    rownum = rownum + 1
print("done")

print("latitude:\n", latitude, " \nlongitude:\n", longitude, "\nelevation:\n", elevation)

latitude, longitude = np.meshgrid(latitude, longitude)

print("latitude:\n", latitude, " \nlongitude:\n", longitude, "\nelevation:\n", elevation)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(latitude, longitude, elevation)

plt.show()

