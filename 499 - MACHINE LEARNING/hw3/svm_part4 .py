# -*- coding: utf-8 -*-
"""svm_part4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8LqOy1-V2iZEWw7HnSWMvGW9TG7_Cqw
"""

#Loading data on Google Colab:
#!wget user.ceng.metu.edu.tr/~artun/ceng499/hw3_files.zip
#!unzip hw3_files.zip

import numpy as np
train_data = np.load ( "/content/hw3/hw3_data/catdogimba/train_data.npy" )
train_labels = np.load ( "/content/hw3/hw3_data/catdogimba/train_labels.npy"  )
test_data = np.load (  "/content/hw3/hw3_data/catdogimba/test_data.npy"  )
test_labels = np.load (  "/content/hw3/hw3_data/catdogimba/test_labels.npy")
print(len(train_data))

def accuracy_calculator(y_pred, y_correct):
  true=0
  false=0
  for i in range(0,len(y_pred)):
    if y_pred[i]==y_correct[i]:
      true=true+1
    elif y_pred[i]!=y_correct[i]:
      false=false+1
  return true/(true+false)

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix,accuracy_score,precision_score,recall_score




from sklearn.utils import shuffle
#shuffle the data
train_data,train_labels= shuffle(train_data,train_labels) 
from sklearn import preprocessing
#normalize the data
train_data = train_data/255
test_data=test_data/255

svclassifier = SVC(kernel='rbf', C=1)
svclassifier.fit(train_data, train_labels)

y_pred = svclassifier.predict(test_data)
print()
print("ACCURACY svm1 = ", accuracy_calculator(y_pred,test_labels))
print()

conf=confusion_matrix(test_labels, y_pred)
print(conf)
print("PRECISION-1= ",precision_score(test_labels, y_pred))
print("RECALL-1= ", recall_score(test_labels, y_pred))



###################################################
###### Oversampling the minority class ############
###################################################

#1- I check what is the minority class
sifir=0
bir=0
for i in range(0,len(train_labels)):
  if train_labels[i]==0:
    sifir=sifir+1
  elif train_labels[i]==1:
    bir=bir+1
print("1--- ",sifir,bir,len(train_labels))

#Multiply minority class
new_train_labels2=[]
new_train_data2=[]

#number of zeros= 215 and number of ones=925, so I need to multiply zeros 4 times

for i in range(0,len(train_labels)):
  if train_labels[i]==0:
    
    #add zeros 4 times 
    new_train_labels2.append(train_labels[i])
    new_train_labels2.append(train_labels[i])
    new_train_labels2.append(train_labels[i])
    new_train_labels2.append(train_labels[i])

    new_train_data2.append(train_data[i])
    new_train_data2.append(train_data[i])
    new_train_data2.append(train_data[i])
    new_train_data2.append(train_data[i])   
  elif train_labels[i]==1:
    new_train_labels2.append(train_labels[i])
    new_train_data2.append(train_data[i])

print(len(new_train_labels2))
print(len(new_train_data2))
print("************************")

#Check again the new dataset where 'zeros' are multiplied
sifir=0
bir=0
for i in range(0,len(new_train_labels2)):
  if new_train_labels2[i]==0:
    sifir=sifir+1
  elif new_train_labels2[i]==1:
    bir=bir+1
print("2--- ",sifir,bir,len(new_train_labels2))
#new number of zeros= 860 and new number of ones=925


svclassifier2 = SVC(kernel='rbf', C=1)
svclassifier2.fit(new_train_data2, new_train_labels2)

y_pred2 = svclassifier2.predict(test_data)
print()
print("ACCURACY-2 = ", accuracy_calculator(y_pred2,test_labels))
print()

conf=confusion_matrix(test_labels, y_pred2)
print(conf)
print("PRECISION-2= ",precision_score(test_labels, y_pred2))
print("RECALL-2= ", recall_score(test_labels, y_pred2))



###################################################
###### Undersampling the majority class ############
###################################################

new_train_labels3=[]
new_train_data3=[]

#number of zeros= 215 and number of ones=925, so I need to multiply zeros 4 times
count= 0
for i in range(0,len(train_labels)):
  if train_labels[i]==0:   
    new_train_labels3.append(train_labels[i])   
    new_train_data3.append(train_data[i])

  elif train_labels[i]==1:
    if count<215:
      new_train_labels3.append(train_labels[i])
      new_train_data3.append(train_data[i])
      count=count+1

print("len(new_train_labels3) = ",len(new_train_labels3))
print("len(new_train_data3) = ",len(new_train_data3))
#Now, the number of zeros=215, the number of ones=215 in the dataset

svclassifier3 = SVC(kernel='rbf', C=1)
svclassifier3.fit(new_train_data3, new_train_labels3)


y_pred3 = svclassifier3.predict(test_data)
print()
print("ACCURACY-3 = ", accuracy_calculator(y_pred3,test_labels))
print()

conf=confusion_matrix(test_labels, y_pred3)
print(conf)
print("PRECISION-3= ",precision_score(test_labels, y_pred3))
print("RECALL-3= ", recall_score(test_labels, y_pred3))
###################################################
###### class_weigh = "balanced" ###################
###################################################

svclassifier4 = SVC(kernel='rbf', C=1, class_weight= "balanced")
svclassifier4.fit(train_data, train_labels)

y_pred4 = svclassifier4.predict(test_data)
print()
print("ACCURACY-4 = ", accuracy_calculator(y_pred4,test_labels))
print()
conf=confusion_matrix(test_labels, y_pred4)
print(conf)
print("PRECISION-4= ",precision_score(test_labels, y_pred4))
print("RECALL-4= ", recall_score(test_labels, y_pred4))