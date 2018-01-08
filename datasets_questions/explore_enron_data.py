#!/usr/bin/python

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

print len(enron_data)

poiCount = 0
validSalaryCount = 0
validEmailCount = 0
emptyPaymentsCount = 0
for key, value in enron_data.items():
    print(key, value)
    if value.get("poi"):
        poiCount += 1
    if value.get("salary") != "NaN":
        validSalaryCount += 1
    if value.get("email_address") != "NaN":
        validEmailCount += 1
    if value.get("total_payments") == "NaN" and value.get("poi"):
        emptyPaymentsCount += 1

print poiCount
print validSalaryCount
print validEmailCount
print emptyPaymentsCount
print float(emptyPaymentsCount) / len(enron_data)
print enron_data['PRENTICE JAMES']['total_stock_value']
