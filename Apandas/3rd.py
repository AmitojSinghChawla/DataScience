import numpy as np
import pandas as

#A Way to Overcome the obstacle of Pycharm Not Showing data in Default Settings
desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

university=pd.read_csv('top 100 world university 2024 new.csv')
university_df=pd.DataFrame(university)
n_rows = 10
n_columns = 7
subset = university_df.head(n_rows).iloc[:, :n_columns]
print(subset)

#7th Continuing the panda features from california data bases