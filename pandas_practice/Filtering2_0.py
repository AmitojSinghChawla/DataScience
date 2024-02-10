import numpy as np
import pandas as pd
import seaborn as sns
#A Way to Overcome the obstacle of Pycharm Not Showing complete data in Default Settings
desired_width=400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',20)

ship=sns.load_dataset("titanic")

#now we create a datafram from this data
n_rows = 100
n_columns = 11
subset = ship.head(n_rows).iloc[:, :n_columns]
#print(subset)




#filtering\
age= (ship["age"] >50)
am= (ship.loc[age,"sex"].tolist()) #gives me a list of sex of all the people above the age of 50

dataset=pd.read_csv("cars.csv")
dataset_df=pd.DataFrame(dataset)
#print(dataset_df.head())


#filter
car=["Honda","Maruti Suzuki","Nissan"]
h=dataset_df["Make"].isin(car)

print(dataset_df.loc[h,"Location"])
#The above filter has first filtered out all the cars which are of the Make of the provided Names in String list Cars then Loc funtion finds them according to "h" and then prints along their location


#filter(IMPORTANT)
# this allows us to find a specific literal value in a column which has multiple values separated by a colon eg
# filt= df["COlUMN NAME"].str.contains("Value",na=False)

# df.loc[filt]

#the filt value here searches the column name in the dataset df and checks if in the string values of the tha column there exsists a specifi "Value" and returns true if there is and false if not . na=false provides the statment that if the column has no value then the conditional statement would return false.

# then the loc function locates the TRUE values from the condition statemnet


#(Very Very Important)
# The diffrence between iloc and loc is that loc can locate values based on a string input which iloc only takes an integer input to return column value










