# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:29:06 2016

@author: zhuxiaodong
"""

import csv
import pickle

def split_couponid():
    coupon_id1 = {}
    coupon_id2 = {}
    coupon_id3 = {}
    # ---------- coupon_info -----------
    coupon_info = {}
    csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
    lines = csv.reader(csvfile)
    for line in lines:
        if line[2] == 'null':
            continue
        if not coupon_info.has_key(line[2]):
            coupon_info[line[2]] = []
        tmp = []
        tmp.append(line[0])
        tmp.append(line[1])
        tmp.extend(line[3:])
        coupon_info[line[2]].append(tmp)
    csvfile.close() 
    
    # ---------- merchant_info -----------
    merchant_info = {}
    csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
    lines = csv.reader(csvfile)
    for line in lines:
        if not merchant_info.has_key(line[1]):
            merchant_info[line[1]] = []
        tmp = []
        tmp.append(line[0])
        tmp.extend(line[2:])
        merchant_info[line[1]].append(tmp)
    csvfile.close()
    
    csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_test.csv','rU')
    lines = csv.reader(csvfile)
    for line in lines:
        if coupon_info.has_key(line[2]):
            coupon_id3[line[2]] = 0
        if not coupon_info.has_key(line[2]) and not merchant_info.has_key(line[1]):
            coupon_id1[line[2]] = 0
        if not coupon_info.has_key(line[2]) and merchant_info.has_key(line[1]):
            coupon_id2[line[2]] = 0
    csvfile.close()
    
    return coupon_id1,coupon_id2,coupon_id3
    
coupon_id1,coupon_id2,coupon_id3 =  split_couponid()   
    
# store pickle
f = file('../../ccf_data/statistic_analysis/coupon_id2.pkl','wb')
pickle.dump(coupon_id2,f)
f.close()   
    
# store pickle
f = file('../../ccf_data/statistic_analysis/coupon_id3.pkl','wb')
pickle.dump(coupon_id3,f)
f.close()     
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

