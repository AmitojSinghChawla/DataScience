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


plt.plot(x,y,color="b",linestyle="--",marker=".", label="Graph1")
# LABEL  is a way for legend function of plotlib to understand which graph is which and display on the top corner of the graph
# COlOR adds colour to that specific graph
#Linestyle adds what type of line would represne the graph
#Marker are dots representing the pont of P(x,y) in the graph like
# you can check all these designs on the website

plt.plot(x1,y1, label ="Graph2")

plt.xlabel("Ages")
plt.ylabel("Factor")

# adds a title ot the page
plt.title("Sample Data")


#legend helps us to identify which graph is which
# plt.legend(['graph1','graph2']) one way to define legend or you can directly label the graphs while plotting them.
plt.legend()

#grid adds a grid to the graph
plt.grid(True)


# plot styles this shows all of them inbuilt in matplpotlib
#print(plt.style.available)


#saving the plot as png
# plt.savefig('plt.png')

plt.fill_between

plt.show()