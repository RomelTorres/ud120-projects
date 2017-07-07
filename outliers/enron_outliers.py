#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import pprint
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


# read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r"))

del data_dict["TOTAL"]
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

salary = data[:-1, 0]
bonus = data[:-1, 1]

for name in data_dict:
    if ((data_dict[name]["bonus"] > 5000000) and (data_dict[name]["salary"] > 1000000) and
        (data_dict[name]["bonus"] != 'NaN' or data_dict[name]["salary"] != 'NaN')):
        print("The outlier is: {} with bonus: {} and salary:{}".format(
            name, data_dict[name]["bonus"], data_dict[name]["salary"]))

matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
