#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

skip_initial_plot = True

features_train, labels_train, features_test, labels_test = makeTerrainData()

grade_fast = [features_train[ii][0] for ii in range(0, len(features_train))
              if labels_train[ii] == 0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train))
              if labels_train[ii] == 0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train))
              if labels_train[ii] == 1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train))
              if labels_train[ii] == 1]


# initial visualization

if not skip_initial_plot:
    print("Initial plot, close to continue...")
    plt.xlim(0.0, 1.0)
    plt.ylim(0.0, 1.0)
    plt.scatter(bumpy_fast, grade_fast, color="b", label="fast")
    plt.scatter(grade_slow, bumpy_slow, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.show()


clf = AdaBoostClassifier(n_estimators=600, learning_rate=0.1)
clf.fit(features_train, labels_train)
predictions = clf.predict(features_test)
accuracy = accuracy_score(labels_test, predictions)

print("Got an accuracy of: {}%".format(accuracy*100))
try:
    print("Creating and saving a picture of the classifier...")
    prettyPicture(clf, features_test, labels_test)
except NameError:
    print("Error happened")
    pass
