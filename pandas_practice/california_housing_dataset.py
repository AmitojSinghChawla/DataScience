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
#print(california_df.value_counts('AveOccup'))
#this gives us no of times a same value has occured( in this case it is giving us the no of houses having the same no of occupanets)

#7th
#print(california_df.count())# gives us the total no of values in each cloumn

#8th
print(california_df.mean())#gives mean value of each column

#9th
print(california_df.std())#gives us standard deviation column vise

#10th max and min values in each column
print(california_df.max())
print(california_df.min())

#11th instead of doing seprate queries we can get all these statistical data by describe method
print(california_df.describe())


#manuplation of data check world cup scores dataset for this
















