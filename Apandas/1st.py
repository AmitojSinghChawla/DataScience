import numpy as np
import pandas as pd

desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

#first importing a dataset in this case is california housing dataet
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

#now we create a datafram from this data
california_df=pd.DataFrame(housing.data , columns = housing.feature_names)
n_rows = 10
n_columns = 7
subset = california_df.head(n_rows).iloc[:, :n_columns]
print(subset)


#1st finding no of rows and columns
# print(california_df.head())# gives first 5 rows

#2nd
print(california_df.shape)#retuns with no of rows nad colums in the dataset

#3rd
# print(california_df.tail())#prints the last 5 rows of the data frame

#4th
# print(california_df.info())

#5th
#print(california_df.isnull().sum( ))#gievs the sum of null values in each of the feature colums in this case they are 0

#6th
print(california_df.value_counts('AveOccup'))
#this gives us no of times a same value has occured( in this case it is giving us the no of houses having the same no of occupanets)

#7th
print(california_df.groupby('AveOccup').mean())
















