#!/usr/bin/python
"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

features_train, features_test, labels_train, labels_test = preprocess()
# Initialize the Gaussian Naive Bayes class
gnb = GaussianNB()
# Fit the model using the trainning data and time it
t0 = time()
gnb.fit(features_train, labels_train)
t1 = time()
# Predict the possible values of the testing set and time it
t0_predicting = time()
predictions = gnb.predict(features_test)
t1_predicting = time()
# Calculate the accuracy of the model.
accuracy = accuracy_score(labels_test, predictions)
print("Trainning time {}s  with an accuracy of: {}%".format(round(t1-t0),accuracy*100))
print("Predicting is about {} times faster than trainning".format(round(t1-t0)/round(t1_predicting, t0_predicting)))
