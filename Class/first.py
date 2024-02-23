import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.feature_selection as RFE
from sklearn.tree import DecisionTreeClassifier

desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)


cancer=pd.read_csv("data.csv")
print(cancer.head())

# cancer.dropna(axis=1,inplace=True)
# cancer.dropna(axis=0,inplace=True)

x=cancer.drop(columns=["diagnosis"],axis=1)
y=cancer["diagnosis"]
# y=cancer.iloc[:,:-1].values
# x=cancer.iloc[:,:-1].values

print(x)
print(y)


from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.33, random_state=10)


# using pearsons coefficient

cor=X_train.corr()
plt.figure(figsize=(12,10))
sns.heatmap(cor,annot=True,)


rfe = RFE(estimator=DecisionTreeClassifier(), n_features_to_select=3)
rfe.fit(x, y)
for i, col in zip(range(x.shape[1]), x.columns):
    print(f"{col} selected={rfe.support_[i]} rank={rfe.ranking_[i]}")

plt.show()

