import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#importing the internal datasets of seaborn library

tips=sns.load_dataset("tips")
print(tips.head())

# you can use matplot lib functions here also but seabron is bit easier to use than it.
sns.lineplot(x="total_bill",y="tip",data=tips,hue="smoker",style="sex",markers=["o",">"])
# the hue attribute breaks the graph into smoker and non smoker
#the style attribute further breaks the lines into male and female as we have given the value sex it can be smoker or any other attribute
#so in all we have created a graph between tips and total bill and plotted lines for Smoker, Non Smoker which is further divided into male or female
# markers attribute has given male values as o and female values as >

plt.grid()
plt.title("new graph")
plt.show()