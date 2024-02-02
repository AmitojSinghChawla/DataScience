import numpy as np
import pandas as pd

#A Way to Overcome the obstacle of Pycharm Not Showing complete data in Default Settings
desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

gaddiyan=pd.read_csv('cars.csv')
gaddiyan_df=pd.DataFrame(gaddiyan)
n_rows = 10
n_columns = 7
df = gaddiyan_df.head(n_rows).iloc[:, :n_columns]
# print(df)
# print()

#filtering practices

# #1st here it gives us boolean values to our if condition that is if at index 0 cars has a fuel type petrol it returns true
# a= (df['Fuel Type'] == 'Petrol')
# print(a)
#
# #2nd here it shows us all those rows where the condition is true that is car has a petrol fuel type
# print(df[a])

#3rd
#to be continued later

