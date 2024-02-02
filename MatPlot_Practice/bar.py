import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

data=pd.read_csv("cars1.csv")
data_df=pd.DataFrame(data)
rows=30
columns=10
subset = data_df.head(rows).iloc[:, :columns]
#print(subset)

locations=subset["Location"].unique()
#print(locations)
count=subset["Location"].value_counts()
count_list=count.tolist()
#print(count_list)


fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.bar(locations,count_list)
ax.set_xlabel('LOCATIONS')
ax.set_ylabel('NO OF CARS')
print(plt.show())