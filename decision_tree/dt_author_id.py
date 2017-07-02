#!/usr/bin/python

"""
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:
    Sara has label 0
    Chris has label 1
"""
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

skip = False
features_train, features_test, labels_train, labels_test = preprocess()

print(len(features_train[0]))

if not skip:
    clf = DecisionTreeClassifier(random_state=0)
    t0 = time()
    clf.fit(features_train, labels_train)
    t1 = time()
    predictions = clf.predict(features_test)
    accuracy = accuracy_score(labels_test, predictions)
    print("Trainning time {}s  with an accuracy of: {}%".format(round(t1-t0), accuracy*100))
