import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

titanic_df = sns.load_dataset('titanic')

#now we create a datafram from this data
n_rows = 10
n_columns = 7
subset = titanic_df.head(n_rows).iloc[:, :n_columns]
print(subset)

sns.set_style()
order1=["3","2","1"]
sns.barplot(x="pclass",y="age",data=titanic_df,hue="sex",hue_order=["female","male"],order=order1)
# you can make a horizontal bar plot by using orientation attribute in the statments but you need to have a numerical value in both x and y axis
#palette attribute gives predifned colours for the graph just like plt.style.use attribute

plt.show()



