import pylab as pl
from matplotlib import pyplot as plt
import numpy as np

# this gives formatting style to the graph
plt.style.use('Solarize_Light2') # this is from the below plt styles
# avaiable function

x=[10,20,30,40,50]
y=[62,78,81,99,108]

x1=[12,22,33,44,55]
y1=[67,74,81,95,111]

plt.bar(x,y ,label ="Graph1")

plt.bar(x1,y1, label ="Graph2")
plt.legend()
plt.show()