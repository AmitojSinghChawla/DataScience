import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


#reading the data from csv
data=pd.read_csv("sonar_data.csv",header=None)
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


#counting the data for rocks and mines individually

#print(data_df[60].value_counts())

# we go M=108 and R=94 and as both of them have similar no of examples it is better for our machine laerning model
#but for good learning data should be way more


#now we seperate the target value and features from the dataset
X=data_df.drop(columns=60,axis=1)
Y=data_df[60]

# print(X)
# print(Y)


#training and testing the data

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=4)

#print(X.shape, X_train.shape, X_test.shape)



#Model training(logistic regression)

model = LogisticRegression()

model.fit(X_train, Y_train)


#Model Evaluation using the accuracy function from sklearn (more data to train more accuracy)

X_train_prediction = model.predict(X_train)

training_accuracy = accuracy_score(X_train_prediction, Y_train)

#print("Accuracy checking on the data which is already trained upon----->",training_accuracy)

X_test_prediction = model.predict(X_test)

testing_accuracy = accuracy_score(X_test_prediction, Y_test)

#print("This is what accuracy is of the model on the new data provided--->",testing_accuracy)

# Accuracy checking on the data which is already trained upon-----> 0.8453038674033149
# This is what accuracy is of the model on the new data provided---> 0.7619047619047619


#Now Making a Predicition System

input_data=(0.0522,0.0437,0.0180,0.0292,0.0351,0.1171,0.1257,0.1178,0.1258,0.2529,0.2716,0.2374,0.1878,0.0983,0.0683,0.1503,0.1723,0.2339,0.1962,0.1395,0.3164,0.5888,0.7631,0.8473,0.9424,0.9986,0.9699,1.0000,0.8630,0.6979,0.7717,0.7305,0.5197,0.1786,0.1098,0.1446,0.1066,0.1440,0.1929,0.0325,0.1490,0.0328,0.0537,0.1309,0.0910,0.0757,0.1059,0.1005,0.0535,0.0235,0.0155,0.0160,0.0029,0.0051,0.0062,0.0089,0.0140,0.0138,0.0077,0.0031)

#first we convert the data into a numpy arra for a faster processing

input=np.asarray(input_data)

# using my data which i cut pastsed from the orignal to test.csv please refer to that


input_value = input.reshape(1, -1)

prediction=model.predict(input_value)

if(prediction[0]=="R"):
    print("The Object is a Rock")
else:
    print("The Object is a Mine")
