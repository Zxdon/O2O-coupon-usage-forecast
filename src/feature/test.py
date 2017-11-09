# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 20:51:32 2016

@author: Administrator
"""
import csv
import sys
sys.path.append('../common_function')
import common_function

#info = [1,1,1,0,0,0,1,1,1,0,0,0,1,1,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,1,1,0,0]
#train_sample1 = common_function.readCsv('train_sample',7,True)
'''
count = 0
csvfile = open('../../ccf_data/feature/train_sample.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    count = count + 1
'''
'''
sample_submission12 = []
sample_submission14 = []
sample_submission15 = []
csvfile = open('../../ccf_data/result/sample_submission12.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    tmp = []
    tmp.extend(line[:3])
    tmp.append(float(line[3]))
    sample_submission12.append(tmp)
csvfile = open('../../ccf_data/result/sample_submission14.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    tmp = []
    tmp.extend(line[:3])
    tmp.append(float(line[3]))
    sample_submission14.append(tmp)
for i in range(len(sample_submission14)):
    tmp = []
    tmp.extend(sample_submission14[i][:3])
    tmp.append((sample_submission12[i][3]+sample_submission14[i][3])/2)
    sample_submission15.append(tmp)
filename = '../../ccf_data/result/sample_submission15.csv'
csvfile = file(filename,'wb')
writer = csv.writer(csvfile)
writer.writerows(sample_submission15)
csvfile.close()
'''
'''
user_info = {}
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if not user_info.has_key(line[0]):
        user_info[line[0]] = []
    user_info[line[0]].append(line[1:])
csvfile.close()
'''
test_user_info = {}
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    key = (line[0],line[1],line[2])
    if not test_user_info.has_key(key):
        test_user_info[key] = []
    test_user_info[key].append(line[-1])
csvfile.close()

test = {}
for key in test_user_info:
    if len(test_user_info[key]) > 1:
        test[key] = test_user_info[key]
        
test_user_info_rule2 = {}
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    key = (line[0],line[1],line[3])
    if not test_user_info_rule2.has_key(key):
        test_user_info_rule2[key] = []
    test_user_info_rule2[key].append(line[-1])
csvfile.close()

test_rule2 = {}
for key in test_user_info_rule2:
    if len(test_user_info_rule2[key]) > 1:
        test_rule2[key] = test_user_info_rule2[key]
        
coupon_info = {}
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    #key = (line[0],line[1],line[2])
    if not coupon_info.has_key(line[2]):
        coupon_info[line[2]] = []
    #test_user_info[key].append(line[-1])
csvfile.close()
coupon_test_info = {}
for key in test:
    if not coupon_test_info.has_key(key[2]):
        coupon_test_info[key[2]] = []

def daydelta(str1, str2):
    import datetime
    return (datetime.datetime.strptime(str1,'%Y%m%d') - datetime.datetime.strptime(str2,'%Y%m%d')).days
    
for key in test_rule2:
    tmp = test_rule2[key]
    last_time = tmp[0]
    for i in range(1,len(tmp)):
        if daydelta(tmp[i],last_time) > 0:
            last_time = tmp[i]
    tmp.append(last_time)
    
rule2 = []
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    key = (line[0],line[1],line[3])
    if test_rule2.has_key(key) and line[-1] != test_rule2[key][-1]:
        rule2.append([line[0],line[2],line[-1],1.0])
    else:
        rule2.append([line[0],line[2],line[-1],-1])
csvfile.close()



   
test_remove_merchant = {}
for key in test:
    test_remove_merchant[(key[0],key[2])] = test[key]
    
result = []
csvfile = open('../../ccf_data/result/sample_submission11.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    tmp = []
    tmp.extend(line[:3])
    tmp.append(float(line[-1]))
    result.append(tmp)
csvfile.close()

count = 0
for i in range(len(result)):
    tmp = result[i]
    key = (tmp[0],tmp[1])
    if test_remove_merchant.has_key(key):      
        if tmp[2] != test_remove_merchant[key][-1]:
            result[i][-1] = 0.995416416546154215
            count += 1
        
filename = '../../ccf_data/result/sample_submission.csv'
csvfile = file(filename,'wb')
writer = csv.writer(csvfile)
writer.writerows(result)
csvfile.close()

























