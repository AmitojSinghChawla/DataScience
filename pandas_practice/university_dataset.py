import numpy as np
import pandas as pd

#A Way to Overcome the obstacle of Pycharm Not Showing data in Default Settings
desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

university1=pd.read_csv('top 100 world university 2024 new.csv')
university_df=pd.DataFrame(university1)
n_rows = 10
n_columns = 7
subset = university_df.head(n_rows).iloc[:, :n_columns]
print(subset)
print()


#def operations_on_dataset():
#complete the main menu


#print(subset.describe())

#deletes a row with index 0 and you have to specify numpy axis 0
#print(subset.drop(index=0,axis=0))

#removes a column rank and like row you have to specify the numpy axis as 1
#print(subset.drop(columns='rank',axis=1))


#locate a row using index value
#print(subset.iloc[2])#gives all values for a paticular row like in this all values regading university of oxford are given output

#column
# print(subset.iloc[:,0] )#gives values for first column
# print()
# print(subset.iloc[:,1]) #gives values for 2nd column and so on
# print()
# print(subset.iloc[:,2])
# print()
# print(subset.iloc[:,3])

#correlation(as all the columns in the dataset are more like variables
# with diffrent values so we can find a correlation between them
#of how with change in value of one column affects the other)

correlation=(subset.drop(columns='university',axis=1))
print(correlation.corr())














