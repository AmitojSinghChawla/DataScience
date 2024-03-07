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


rows =20
columns = 10
subset = data_df.head(rows).iloc[:, :columns]
#print(subset)

#checking the basic statistical measures of the data
#print(data_df.describe())



#print(data_df["species"].value_counts())
#there are 3 diffrent types of species setosa,versicolor,virgincia all of them have 50 examples each




# #now we seperate the target value and features from the dataset
X=data_df.drop(columns='species',axis=1)
Y=data_df["species"]


#we have seperated the target and features
# print(X)
# print(Y)


#training and testing the data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=4)

print(X.shape, X_train.shape, X_test.shape)


#Model training(logistic regression)

model = LogisticRegression()

model.fit(X_train, Y_train)


# #Model Evaluation using the accuracy function from sklearn (more data to train more accuracy)

# X_train_prediction = model.predict(X_train)
# training_accuracy = accuracy_score(X_train_prediction, Y_train)
# print("Accuracy checking on the data which is already trained upon----->",training_accuracy)

#accuracy came out to be 0.9666666666666667


X_test_prediction = model.predict(X_test)

testing_accuracy = accuracy_score(X_test_prediction, Y_test)

print("This is what accuracy is of the model on the new data provided--->",testing_accuracy)


from sklearn.metrics import confusion_matrix,classification_report
import matplotlib.pyplot as plt

# Calculate the confusion matrix
cm = confusion_matrix(Y_test, X_test_prediction)

# Display the confusion matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", cbar=False)
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')

print(classification_report(Y_test,X_test_prediction))
plt.show()


