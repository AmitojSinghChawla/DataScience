import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#reading the data from csv
data=sns.load_dataset("iris")
data_df=pd.DataFrame(data)

desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)


print(data_df.isnull().value_counts())