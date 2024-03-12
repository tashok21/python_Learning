import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score


heart=pd.read_csv("heart1.csv")   #Read the data

X=heart.iloc[1:,1:-1].values
Y=heart.iloc[1:,-1].values
X_train,X_test,Y_train, Y_test=train_test_split(X,Y,test_size=0.3,random_state=0)

#creating the standard scalar

sc=StandardScaler()
sc.fit(X_train)
X_train_std=sc.transform(X_train)
X_test_std=sc.transform(X_test)

#Combine the Trainign and testing data sets
X_combined_std=np.vstack((X_train_std, X_test_std))
X_combined = np.vstack((X_train,X_test))
Y_combined=np.hstack((Y_train,Y_test))


#Training and Testing for the Machine Learning Algorithms
print("Machine Learning Algorithms:")
print("\n")

#Perceptron model
ppn=Perceptron(max_iter=10, tol=1e-3,eta0=0.001,fit_intercept=True, random_state=0, verbose=True)
ppn.fit(X_train, Y_train) #Training the dataset
Y_pred=ppn.predict(X_test_std)#Testing the dataset
print('Perceptron Model')
print('Accuracy: %.2f' % accuracy_score(Y_test,  Y_pred))
Y_combined_pred = ppn.predict(X_combined_std)
print('Combined Accuracy: %.2f \n' % accuracy_score(Y_combined, Y_combined_pred).sum())

#Logistic Regression
lr = LogisticRegression(C=5, solver='liblinear',multi_class='ovr', random_state=0)
lr.fit(X_train_std, Y_train) 
Y_pred=lr.predict(X_test_std)
print('Logistic Regression')
print('Accuracy: %.2f' % accuracy_score(Y_test,  Y_pred))
Y_combined_pred = lr.predict(X_combined_std)
print('Combined Accuracy: %.2f \n' % accuracy_score(Y_combined, Y_combined_pred).sum())

#SVM
svm = SVC(kernel='linear', C=100, random_state=0)
svm.fit(X_train_std, Y_train)  #Training the dataset
Y_pred = svm.predict(X_test_std)#Testing the data set
print("SVM")
print('Accuracy: %.2f' % accuracy_score(Y_test, Y_pred))
Y_combined_pred = lr.predict(X_combined_std)
print('Combined Accuracy: %.2f \n' % accuracy_score(Y_combined, Y_combined_pred).sum())

#Decision Tree
tree = DecisionTreeClassifier(criterion='entropy',max_depth=50 ,random_state=0)
tree.fit(X_train,Y_train)
Y_pred = tree.predict(X_test)
print("Decision Tree")
print('Accuracy: %.2f' % accuracy_score(Y_test, Y_pred))
Y_combined_pred = tree.predict(X_combined)#Processing the raw data
print('Combined Accuracy: %.2f \n' % accuracy_score(Y_combined, Y_combined_pred))

#Random Forest
forest = RandomForestClassifier(criterion='entropy', n_estimators=10,random_state=1, n_jobs=4)
forest.fit(X_train,Y_train)
Y_pred = forest.predict(X_test) # see how we do on the test data
print("Random Forest")
print('Accuracy: %.2f ' % accuracy_score(Y_test, Y_pred))
Y_combined_pred = forest.predict(X_combined) #Processing the raw data
print('Combined Accuracy: %.2f \n' % accuracy_score(Y_combined, Y_combined_pred))

#KNN
knn = KNeighborsClassifier(n_neighbors=1,p=2,metric='minkowski')
knn.fit(X_train_std,Y_train)
Y_pred = knn.predict(X_test_std)
print("KNN")
print('Accuracy: %.2f' % accuracy_score(Y_test, Y_pred))
Y_combined_pred = knn.predict(X_combined_std)
print('Combined Accuracy: %.2f' % accuracy_score(Y_combined, Y_combined_pred))

#Step1: 3 best methods and prediction:

method1=lr
y_pred_m1 = method1.predict(X_test_std)
method2=tree
y_pred_m2= method2.predict(X_test_std)
method3=svm
y_pred_m3 = method3.predict(X_test_std)
method4=ppn
y_pred_m4 = method4.predict(X_test_std)
method5=knn
y_pred_m5 = method5.predict(X_test_std)

pred_final = y_pred_m1+y_pred_m2+y_pred_m3
thresh = len([method1, method2, method3]) * 1.5
result = np.where(pred_final > thresh, 2, 1)
ensemble_method3 = accuracy_score(Y_test, result )
print(f'Accuracy for three methods: {ensemble_method3:.2%}')

#For 4 methods
pred_final=y_pred_m1+y_pred_m2+y_pred_m3+y_pred_m4 
thresh = len([method1, method2, method3,method4]) * 1.5
result  = np.where(pred_final >= thresh, 2, 1)
ensemble_accuracy_4 = accuracy_score(Y_test,result )
print(f'Accuracy for four methods when ties are considered yes: {ensemble_accuracy_4:.2%}')
result1 = np.where(pred_final > thresh, 2, 1)
ensemble_method4 = accuracy_score(Y_test, result1)
print(f'Accuracy for four methods when ties are considered no: {ensemble_method4:.2%}')

#For 5th method:
pred_final_4=y_pred_m1+y_pred_m2+y_pred_m3+y_pred_m4+y_pred_m5
thresh = len([method1, method2, method3,method4,method5]) * 1.5
result  = np.where(pred_final > thresh, 2, 1)
ensemble_method5 = accuracy_score(Y_test,result )
print(f'Accuracy for five methods: {ensemble_method5:.2%}')








