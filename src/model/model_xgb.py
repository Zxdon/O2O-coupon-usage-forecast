# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:53:15 2016

@author: zhuxiaodong

xgb test
"""

import numpy as np
import xgboost as xgb
import pickle

test_data = pickle.load(open('../../ccf_data/feature/test_data.pkl','rb'))
train_sample = pickle.load(open('../../ccf_data/feature/train_sample.pkl','rb'))
test_sample = pickle.load(open('../../ccf_data/feature/valid_sample.pkl','rb'))

# label need to be 0 to num_class -1
'''
data = np.loadtxt('./dermatology.data', delimiter=',',converters={33: lambda x:int(x == '?'), 34: lambda x:int(x)-1 } )
sz = data.shape

train = data[:int(sz[0] * 0.7), :]
test = data[int(sz[0] * 0.7):, :]
'''
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
    

xg_train = xgb.DMatrix( train_sample_feature, label=train_sample_label)
xg_test = xgb.DMatrix(test_sample_feature, label=test_sample_label)
# setup parameters for xgboost
param = {}
# use softmax multi-class classification
param['objective'] = 'multi:softmax'
# scale weight of positive examples
param['eta'] = 0.1
param['max_depth'] = 6
param['silent'] = 1
param['nthread'] = 4
param['num_class'] = 2

watchlist = [ (xg_train,'train'), (xg_test, 'test') ]
num_round = 10
bst = xgb.train(param, xg_train, num_round, watchlist );
# get prediction
pred = bst.predict( xg_test );

print ('predicting, classification error=%f' % (sum( int(pred[i]) == test_sample_label[i] for i in range(len(test_sample_label))) / float(len(test_sample_label)) ))

# do the same thing again, but output probabilities
param['objective'] = 'multi:softprob'
bst = xgb.train(param, xg_train, num_round, watchlist );
# Note: this convention has been changed since xgboost-unity
# get prediction, this is in 1D array, need reshape to (ndata, nclass)
yprob = bst.predict( xg_test ).reshape( np.array(test_sample_label).shape[0], 2 )
ylabel = np.argmax(yprob, axis=1)

print ('predicting, classification error=%f' % (sum( int(ylabel[i]) == test_sample_label[i] for i in range(len(test_sample_label))) / float(len(test_sample_label)) ))




