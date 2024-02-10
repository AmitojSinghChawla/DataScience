import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
#What is a Histogram?
#--> Histograms are graphical represantion of contious data sets unlike bar graphs
#in this scenario here the histogram is showing us the no of people in a specific range
#of age group.

ages=[18,19,20,21,22,23,26,35,42,55,60]
bins=[0,10,20,30,40,50,60]#bins makes the range in which histogram operates
#here as per our input the range would be 10-20,20-30,30-40,40-50,50-60.
#and in these ranges continuous bars would be shown


plt.hist(ages,bins=bins,edgecolor="black")
plt.show()
