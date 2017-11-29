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


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC

# features_train = features_train[:len(features_train) / 100]
# labels_train = labels_train[:len(labels_train) / 100]

clf = SVC(C=10000, kernel="rbf")

t0 = time()
clf.fit(features_train, labels_train)
print "train time:", round(time() - t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "predict time:", round(time() - t0, 3), "s"

num = 0
count = 0
for p in pred:
    if p == 1:
        num += 1
    count += 1

print("num:%d  sum:%d" % (num, count))
from sklearn.metrics import accuracy_score

score = accuracy_score(pred, labels_test)
print(score)

### linear
### all data accuracy 0.984 ###
### 1% data accuracy 0.884(C = 1.0) ###
### 1% data accuracy 0.874(C = 10.0) ###
### 1% data accuracy 0.861(C = 100.0) ###
### 1% data accuracy 0.861(C = 10000.0) ###
### 1% data accuracy 0.878(C = 0.8) ###
#########################################################
