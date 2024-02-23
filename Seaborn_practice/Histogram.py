import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

tip= sns.load_dataset("tips")
rows =50
columns = 10
subset = tip.head(rows).iloc[:, :columns]
#print(subset)

sns.histplot(data=tip,x="total_bill", bins=10)
plt.show()
