#Imagine you have two lists of numbers, like the amount of time people spend studying and their test scores. A scatter plot lets you plot these numbers on a graph with one list on the x-axis (horizontal) and the other on the y-axis (vertical).
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#The points on the graph show where each pair of numbers is located. If most of the points are clustered together in a line that goes from the bottom-left to the top-right, it means there's a positive relationship between the two sets of data. This means that as one variable increases, the other tends to increase too. If the points are scattered all over the place with no clear pattern, it means there's no strong relationship between the two variables.

#Scatter plots are different from other types of graphs, like bar graphs or line graphs, because they specifically show how two sets of data are related to each other, rather than just showing individual values or trends over time. They're really useful for spotting patterns and relationships in data!)
desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

stats=pd.read_csv("dummy_data.csv")
stats_df=pd.DataFrame(stats)

#print(stats_df.head(10).iloc[:, :10])
filt=(stats_df["location"]== "Australia")

filt_df=stats_df.loc[filt]
timepent=filt_df.head(50)["time_spent"].dropna().tolist()
ages=filt_df.head(50)["ages"].dropna().tolist()
incom=filt_df.head(50)["income"].dropna().tolist()
# print(timepent)
# print(ages)

plt.scatter(timepent,ages,edgecolor="black",alpha=0.76,size=incom)
plt.show()