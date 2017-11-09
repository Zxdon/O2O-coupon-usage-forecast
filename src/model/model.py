# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:25:24 2016

@author: zhuxiaodong 

create model

"""
import csv
import pickle
import sys
sys.path.append('../common_function')
import common_function

import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn.metrics import roc_curve, auc
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
#from sklearn.neural_network import MLPClassifier
#from sklearn.svm import SVR

test_data = pickle.load(open('../../ccf_data/feature/test_data.pkl','rb'))
#train_sample = common_function.readCsv('train_sample')
#test_sample = common_function.readCsv('test_sample')
train_sample = pickle.load(open('../../ccf_data/feature/train_sample.pkl','rb'))
test_sample = pickle.load(open('../../ccf_data/feature/valid_sample.pkl','rb'))


train_sample_info = []
train_sample_feature = []
train_sample_label = []

for i in range(len(train_sample)):
    train_sample_info.append(train_sample[i][:7])
    train_sample_feature.append(train_sample[i][7:-1])
    train_sample_label.append(train_sample[i][-1])

test_sample_info = []
test_sample_feature = []
test_sample_label = []

for i in range(len(test_sample)):
    test_sample_info.append(test_sample[i][:7])
    test_sample_feature.append(test_sample[i][7:-1])
    test_sample_label.append(test_sample[i][-1])

min_max_scaler = preprocessing.MinMaxScaler()
train_sample_feature = min_max_scaler.fit_transform(train_sample_feature)
#clf = MLPClassifier(hidden_layer_sizes=(8, 4), max_iter=50, alpha=1e-4,
#                     solver='sgd', verbose=10, tol=1e-4, random_state=1)
clf = LogisticRegression(penalty='l2', C=8, class_weight={0: 1, 1: 3})
#clf = GradientBoostingClassifier(n_estimators = 200)
#clf = RandomForestClassifier(n_estimators = 50)
#clf = SVC(C = 0.8,probability = True)
#clf = SVC(kernel='poly')
#scores_lr = cross_validation.cross_val_score(clf, np.array(train_sample_feature), np.array(train_sample_label), cv=10)

# shuffle and split training and test sets
#X_train, X_test, y_train, y_test = train_test_split(train_sample_feature, train_sample_label, test_size=.1,
#                                                    random_state=0)
clf.fit(train_sample_feature, train_sample_label)  
#print clf.feature_importances_   
print clf                                               

test_sample_feature = min_max_scaler.fit_transform(test_sample_feature)
score = clf.score(test_sample_feature, test_sample_label)
score_train = clf.score(train_sample_feature, train_sample_label)

                                                                                                   
# Learn to predict each class against the other  
test_sample_feature_proba = clf.predict_proba(test_sample_feature)                                                                                                   
#y_score = clf.decision_function(test_sample_feature)
y_score = test_sample_feature_proba[:,1]

valid_submit = []
for i in range(len(test_sample_info)):
    tmp = []
    tmp.append(test_sample_info[i][0])
    tmp.append(test_sample_info[i][2])
    tmp.append(test_sample_info[i][-1])
    tmp.append(y_score[i])
    valid_submit.append(tmp)
common_function.valid_submit_eval(valid_submit,test_sample_label)
# Compute ROC curve and ROC area for each class
fpr = dict()
tpr = dict()
roc_auc = dict()
fpr, tpr, _ = roc_curve(test_sample_label, y_score)
roc_auc = auc(fpr, tpr)
print 'roc_auc:%f' %roc_auc
'''
# Plot of a ROC curve for a specific class
plt.figure()
plt.plot(fpr, tpr, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()

#test_sample_feature_proba = clf.predict(test_sample_feature)
lr_proba = [x[1] for x in test_sample_feature_proba]
result_lr = []
for i in range(len(lr_proba)):
    if lr_proba[i] > 0.5:
        result_lr.append(1)
    else:
        result_lr.append(0)
        
pos_num = 0
pos_num_real = 0
for i in range(len(result_lr)):
    if result_lr[i] == 1:
        pos_num = pos_num + 1
for i in range(len(test_sample_label)):
    if test_sample_label[i] == 1:
        pos_num_real = pos_num_real + 1
correct = 0        
for i in range(len(result_lr)):
    if result_lr[i] == 1 and result_lr[i] == test_sample_label[i]:
        correct = correct + 1
print 'precise:%f' %(correct*1.0/pos_num)
print 'recall:%f' %(correct*1.0/pos_num_real)
print 'f:%f' %(2*(correct*1.0/pos_num)*(correct*1.0/pos_num_real)/((correct*1.0/pos_num) + (correct*1.0/pos_num_real)))

correct = 0        
for i in range(len(result_lr)):
    if result_lr[i] == test_sample_label[i]:
        correct = correct + 1
print 'accuracy:%f' %(correct*1.0/len(result_lr))
'''
test_data_info = []
test_data_feature = []   
for i in range(len(test_data)):
    test_data_info.append(test_data[i][:6])
    test_data_feature.append(test_data[i][6:])  
lr_proba = []   
test_data_feature = min_max_scaler.transform(test_data_feature)
test_prob = clf.predict_proba(np.array(test_data_feature))
lr_proba = [x[1] for x in test_prob]

tmp = []
for i in range(len(test_data_info)):
    tmp1 = []
    tmp1.append(test_data_info[i][0])
    tmp1.append(test_data_info[i][2])
    tmp1.append(test_data_info[i][-1])
    tmp1.append(lr_proba[i])
    tmp.append(tmp1)

filename = '../../ccf_data/result/sample_submission.csv'
csvfile = file(filename,'wb')
writer = csv.writer(csvfile)
writer.writerows(tmp)
csvfile.close()









