import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

dataa=pd.read_csv('Placement_Dataset.csv')
data_df=pd.DataFrame(dataa)

# data_df=sns.load_dataset("")
rows =10
columns = 20
subset = data_df.head(rows).iloc[:, :columns]
print(subset)
# print(data_df.isnull().sum())
#now that we know how many missing values there are we can either drop them or we can imputate data there
#here as we dont have a very big dataset we impute data into it using central tendencies in it (mean,median,mode)


#we need to analyse it frst before deciding how to impute the data
#for it le us first visualise the the data

#USING THE SUPLOT METHOD
sns.displot(data=data_df,x="salary",)

#AFTER visualising the data we saw that the slaries were skewed positively hence we cant use mean imputation method in here
#beacuse of unequal influence of diffrent salary values to the mea (you can run the graph and see for yourself)
#plt.show()




#imputation via median method

#this is one method but use the other one now

data_df["salary"].fillna(data_df["salary"].median(),inplace=True)


# print(data_df.isnull().sum())
#we have replaced the missing values

