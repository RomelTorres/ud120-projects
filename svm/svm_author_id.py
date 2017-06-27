#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Parameters
# set to true if you want to reduce the data set training time (but worse results)
reduce_train_set = True
kernel_type = 'rbf'
C = 1.0

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
if reduce_train_set:
    features_train = features_train[1:len(features_train)/100]
    labels_train = labels_train[1:len(labels_train)/100]
# Initialize the Suport Vector Machine class, with a linear Kernel
clf = SVC(C=C)
# Fit the model using the trainning data and time it
t0 = time()
clf.fit(features_train, labels_train)
t1 = time()
# Predict the possible values of the testing set
predictions = clf.predict(features_test)
# Calculate the accuracy of the model.
accuracy = accuracy_score(predictions, labels_test)
print("Trainning time {}s  with an accuracy of: {}%".format(round(t1-t0),accuracy*100))
