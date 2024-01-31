import numpy as np 
import pandas as pd 

#first importing a dataset in this case is california housing dataet
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

#now we create a datafram from this data
california_df=pd.DataFrame(housing.data , columns = housing.feature_names)
california_df.head

print(california_df.shape)








