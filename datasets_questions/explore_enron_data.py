#!/usr/bin/python
import pprint
"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print("Amount of people data: {}".format(len(enron_data)))
jeffrey = enron_data['SKILLING JEFFREY K']

print("Example of a person's data:")
pprint.pprint(jeffrey)
print("Number of features per person: {}".format(len(jeffrey)))
# Calculate how many persons of interest are available in hte data set
pois = 0
for key, value in enron_data.iteritems():
    if enron_data[key]['poi'] is True:
        pois += 1
print('Number of pois: {}'.format(pois))
james = enron_data['PRENTICE JAMES']
print("The total stock value from james is: {}".format(james['total_stock_value']))
wesley = enron_data['COLWELL WESLEY']
print("Wesley sent: {} to pois".format(wesley['from_this_person_to_poi']))

print("The value of stock options exercised by Jeffrey is: {}".format(jeffrey['exercised_stock_options']))

pois_names = ('SKILLING JEFFREY K','LAY KENNETH L', 'FASTOW ANDREW S')

for name in pois_names:
    print("Name: {} took home: {}".format(name, enron_data[name]['total_payments']))


salaries = 0
for key, value in enron_data.iteritems():
    if enron_data[key]['salary'] != 'NaN':
        salaries += 1
print("Total listed salaries: {}".format(salaries))


email = 0
for key, value in enron_data.iteritems():
    if enron_data[key]['email_address'] != 'NaN':
        email += 1
print("Total listed emails: {}".format(email))

tt_payments = 0
for key, value in enron_data.iteritems():
    if enron_data[key]['total_payments'] == 'NaN':
        tt_payments += 1
print("Total listed payments: {}".format(tt_payments))
print("Total listed payments %: {}".format(100.0*tt_payments/len(enron_data)))

tt_payments_poi = 0
for key, value in enron_data.iteritems():
    if enron_data[key]['total_payments'] == 'NaN' and enron_data[key]['poi'] is True:
        tt_payments_poi += 1
print("Total listed payments: {}".format(tt_payments_poi))
print("Total listed payments %: {}".format(100.0*tt_payments_poi/pois))
