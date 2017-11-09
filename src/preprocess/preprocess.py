# -*- coding: utf-8 -*-
"""
Created on Sun Oct 9 16:35:46 2016

@author: zhuxiaodong

step1: read data
step2: preprocess data

"""

import csv
import pickle
import datetime

# ---------- loading original data ------------
# -- note: ccf_data/ccf_offline_stage1_test.csv,ccf_offline_stage1_train.csv, please put the files in the correct path!

# ---------- user_info -----------
user_info = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if not user_info.has_key(line[0]):
        user_info[line[0]] = []
    user_info[line[0]].append(line[1:])
csvfile.close()

'''
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
'''
'''
# -------- 用户的id字典 -------------
user_id = {}
for key in user_info:
    user_id[key] = 0
# store pickle
f = file('../../ccf_data/statistic_analysis/user_id.pkl','wb')
pickle.dump(user_id,f)
f.close()
user_id = {}
# -------- 商店的id字典 -------------
merchant_id = {}
for key in merchant_info:
    merchant_id[key] = 0
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_id.pkl','wb')
pickle.dump(merchant_id,f)
f.close()
merchant_id = {}
# -------- 优惠券的id字典 -------------
coupon_id = {}
for key in coupon_info:
    coupon_id[key] = 0
# store pickle
f = file('../../ccf_data/statistic_analysis/coupon_id.pkl','wb')
pickle.dump(coupon_id,f)
f.close()
coupon_id = {}


# ------- 商店发了那些优惠券 -------
merchant_coupon = {}
for key in merchant_info:
    merchant_coupon[key] = set()
    record = merchant_info[key]
    for row in record:
        if row[1] == 'null':
            continue
        merchant_coupon[key].add(row[1])
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_coupon.pkl','wb')
pickle.dump(merchant_coupon,f)
f.close()
merchant_coupon = {}      
# ------ 优惠券由那些商店发出 -----
coupon_merchant = {}
for key in coupon_info:
    coupon_merchant[key] = set()
    record = coupon_info[key]
    for row in record:
        coupon_merchant[key].add(row[1])
# store pickle
f = file('../../ccf_data/statistic_analysis/coupon_merchant.pkl','wb')
pickle.dump(coupon_merchant,f)
f.close()
coupon_merchant = {}

coupon_test_info = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    coupon_test_info[line[2]] = 0
csvfile.close()

coupon_in_train = {}
coupon_not_in_train = {}
for key in coupon_test_info:
    if coupon_info.has_key(key):
        coupon_in_train[key] = []
    else:
        coupon_not_in_train[key] = []

csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    tmp = []
    tmp.append(line[0])
    tmp.append(line[1])
    tmp.extend(line[3:])
    if coupon_in_train.has_key(line[2]):
        coupon_in_train[line[2]].append(tmp)
    else:
        coupon_not_in_train[line[2]].append(tmp)
csvfile.close()

# ------- 用户普通消费、使用优惠券、未使用优惠券的数量 -------
user_consume_record = {}
for key in user_info:
    common_consume = 0
    use_coupon_consume = 0
    not_use_coupon = 0
    record = user_info[key]
    for row in record:
        if row[1] == 'null' and row[-1] != 'null':
            common_consume = common_consume + 1
        if row[1] != 'null' and row[-1] != 'null':
            use_coupon_consume = use_coupon_consume + 1
        if row[1] != 'null' and row[-1] == 'null':
            not_use_coupon = not_use_coupon + 1
    user_consume_record[key] = [common_consume, use_coupon_consume, not_use_coupon]
# store pickle
f = file('../../ccf_data/statistic_analysis/user_consume_record.pkl','wb')
pickle.dump(user_consume_record,f)
f.close()
user_consume_record = {}

# --------- 用户15日内使用优惠券的数量 和15日外使用优惠券的数量 1 3 7 15-----
user_use_coupon_date_record = {}
for key in user_info:
    user_use_coupon_date_record[key] = [0,0,0,0,0]
    record = user_info[key]
    for row in record:
        if row[1] != 'null' and row[-1] != 'null':
            day = (datetime.datetime(int(row[-1][:4]),int(row[-1][4:6]),int(row[-1][6:])) - \
            datetime.datetime(int(row[-2][:4]),int(row[-2][4:6]),int(row[-2][6:]))).days
            if day < 1:
                user_use_coupon_date_record[key][0] = user_use_coupon_date_record[key][0] + 1
            if day < 3:
                user_use_coupon_date_record[key][1] = user_use_coupon_date_record[key][1] + 1
            if day < 7:
                user_use_coupon_date_record[key][2] = user_use_coupon_date_record[key][2] + 1
            if day < 15:
                user_use_coupon_date_record[key][3] = user_use_coupon_date_record[key][3] + 1
            user_use_coupon_date_record[key][4] = user_use_coupon_date_record[key][4] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/user_use_coupon_date_record.pkl','wb')
pickle.dump(user_use_coupon_date_record,f)
f.close()
user_use_coupon_date_record = {}
'''

'''
# --------- 商店普通消费、使用优惠券、未使用优惠券的数量 -----
merchant_consume_record = {}
for key in merchant_info:
    common_consume = 0
    use_coupon_consume = 0
    not_use_coupon = 0
    record = merchant_info[key]
    for row in record:
        if row[1] == 'null' and row[-1] != 'null':
            common_consume = common_consume + 1
        if row[1] != 'null' and row[-1] != 'null':
            use_coupon_consume = use_coupon_consume + 1
        if row[1] != 'null' and row[-1] == 'null':
            not_use_coupon = not_use_coupon + 1
    merchant_consume_record[key] = [common_consume, use_coupon_consume, not_use_coupon]
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_consume_record.pkl','wb')
pickle.dump(merchant_consume_record,f)
f.close()
merchant_consume_record = {}
# --------- 商店消费一次和多次的用户的id集合 -----
merchant_user_consume_number_record = {}
for key in merchant_info:
    merchant_user_consume_number_record[key] = [set(), set()]
    record = merchant_info[key]
    for row in record:
        if row[-1] != 'null':
            if (row[0] in merchant_user_consume_number_record[key][0]) and \
                (row[0] not in merchant_user_consume_number_record[key][1]):
                merchant_user_consume_number_record[key][0].remove(row[0])
                merchant_user_consume_number_record[key][1].add(row[0])
            if (row[0] not in merchant_user_consume_number_record[key][0]) and \
                (row[0] not in merchant_user_consume_number_record[key][1]):
                merchant_user_consume_number_record[key][0].add(row[0])
            
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_user_consume_number_record.pkl','wb')
pickle.dump(merchant_user_consume_number_record,f)
f.close()
merchant_user_consume_number_record = {}
# --------- 商店普通消费的但未使用优惠券的id集合，消费且使用过优惠券的id集合 -----
merchant_user_consume_record = {}
for key in merchant_info:
    merchant_user_consume_record[key] = [set(), set()]
    record = merchant_info[key]
    for row in record:
        if row[-1] != 'null':
            if row[1] == 'null': #普通消费
                if (row[0] not in merchant_user_consume_record[key][0]) and \
                (row[0] not in merchant_user_consume_record[key][1]):
                    merchant_user_consume_record[key][0].add(row[0])
            else: #优惠券消费
                if row[0] in merchant_user_consume_record[key][0]:
                    merchant_user_consume_record[key][0].remove(row[0])
                    merchant_user_consume_record[key][1].add(row[0])
                if (row[0] not in merchant_user_consume_record[key][0]) and \
                (row[0] not in merchant_user_consume_record[key][1]):
                    merchant_user_consume_record[key][1].add(row[0])     
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_user_consume_record.pkl','wb')
pickle.dump(merchant_user_consume_record,f)
f.close()
merchant_user_consume_record = {}

# --------- 用户惠顾惠顾商店的id和次数 ----------
user_merchant_consume_number_record = {}
for key in user_info:
    user_merchant_consume_number_record[key] = {}
    record = user_info[key]
    for row in record:
        if row[-1] != 'null':
            if not user_merchant_consume_number_record[key].has_key(row[0]):
                user_merchant_consume_number_record[key][row[0]] = 0
            user_merchant_consume_number_record[key][row[0]] = \
            user_merchant_consume_number_record[key][row[0]] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/user_merchant_consume_number_record.pkl','wb')
pickle.dump(user_merchant_consume_number_record,f)
f.close()
user_merchant_consume_number_record = {}

# --------- 用户惠顾惠顾商店的id，普通消费次数 、优惠券消费次数、未使用优惠券消费次数----------
user_merchant_record = {}   
for key in user_info:
    user_merchant_record[key] = {}
    record = user_info[key]
    for row in record:
        if not user_merchant_record[key].has_key(row[0]):
            user_merchant_record[key][row[0]] = [0,0,0]
        if row[1] == 'null' and row[-1] != 'null':
            user_merchant_record[key][row[0]][0] = \
            user_merchant_record[key][row[0]][0] + 1
        if row[1] != 'null' and row[-1] != 'null':
            user_merchant_record[key][row[0]][1] = \
            user_merchant_record[key][row[0]][1] + 1
        if row[1] != 'null' and row[-1] == 'null':
            user_merchant_record[key][row[0]][2] = \
            user_merchant_record[key][row[0]][2] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/user_merchant_record.pkl','wb')
pickle.dump(user_merchant_record,f)
f.close()
user_merchant_record = {}

#-------- 满x减y的优惠券的使用情况 --------
XtoYcategory_use_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if len(line[3].split(':')) == 2:
        if not XtoYcategory_use_record.has_key(line[3]):
            XtoYcategory_use_record[line[3]] = [0,0]
        if line[-1] != 'null':
            XtoYcategory_use_record[line[3]][0] = XtoYcategory_use_record[line[3]][0] + 1
        XtoYcategory_use_record[line[3]][1] = XtoYcategory_use_record[line[3]][1] + 1
csvfile.close()
# store pickle
f = file('../../ccf_data/statistic_analysis/XtoYcategory_use_record.pkl','wb')
pickle.dump(XtoYcategory_use_record,f)
f.close()
XtoYcategory_use_record = {}

#-------给优惠种类加上index-----------
XtoYcategory_index = {}
count = 0
for key in XtoYcategory_use_record:
    XtoYcategory_index[key] = count
    count = count + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/XtoYcategory_index.pkl','wb')
pickle.dump(XtoYcategory_index,f)
f.close()
    
#-------- 折扣的优惠券的种类使用情况 --------
discountCategory_use_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if line[3] != 'null' and len(line[3].split(':')) == 1:
        if not discountCategory_use_record.has_key(line[3]):
            discountCategory_use_record[line[3]] = [0,0]
        if line[-1] != 'null':
            discountCategory_use_record[line[3]][0] = discountCategory_use_record[line[3]][0] + 1
        discountCategory_use_record[line[3]][1] = discountCategory_use_record[line[3]][1] + 1
csvfile.close()
# store pickle
f = file('../../ccf_data/statistic_analysis/discountCategory_use_record.pkl','wb')
pickle.dump(discountCategory_use_record,f)
f.close()
discountCategory_use_record = {}

#-------给优惠种类加上index-----------
discountCategory_index = {}
count = 0
for key in discountCategory_use_record:
    discountCategory_index[key] = count
    count = count + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/discountCategory_index.pkl','wb')
pickle.dump(discountCategory_index,f)
f.close()

#-------- 按照距离优惠券的使用情况 --------
coupon_distance_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if line[2] == 'null':
        continue
    if not coupon_distance_record.has_key(line[4]):
        coupon_distance_record[line[4]] = [0,0]
    if line[-1] != 'null':
        coupon_distance_record[line[4]][0] = coupon_distance_record[line[4]][0] + 1
    coupon_distance_record[line[4]][1] = coupon_distance_record[line[4]][1] + 1     
csvfile.close()
# store pickle
f = file('../../ccf_data/statistic_analysis/coupon_distance_record.pkl','wb')
pickle.dump(coupon_distance_record,f)
f.close()
coupon_distance_record = {}
#-------- 按照距离优惠券的使用比例 --------
coupon_distance_consume_ratio_record = {}
for key in coupon_distance_record:
    coupon_distance_consume_ratio_record[key] = coupon_distance_record[key][0] * 1.0/coupon_distance_record[key][1]
# store pickle
f = file('../../ccf_data/statistic_analysis/coupon_distance_consume_ratio_record.pkl','wb')
pickle.dump(coupon_distance_consume_ratio_record,f)
f.close()
coupon_distance_consume_ratio_record = {}

# ------ 用户根据距离使用优惠券的情况 ------
# 0/1-2/3-5/6-10/null
user_use_coupon_according_distance_record = {}
for key in user_info:
    tmp = {}
    for i in range(5):
        tmp[i] = [0,0]
    record = user_info[key]
    for row in record:
        if row[1] == 'null':
            continue
        if row[3] == 'null':
            if row[-1] != 'null':
                tmp[4][0] = tmp[4][0] + 1
            tmp[4][1] = tmp[4][1] + 1
            continue
        if int(row[3]) == 0:
            if row[-1] != 'null':
                tmp[0][0] = tmp[0][0] + 1
            tmp[0][1] = tmp[0][1] + 1
            continue
        if int(row[3]) >= 1 and int(row[3]) <= 2:
            if row[-1] != 'null':
                tmp[1][0] = tmp[1][0] + 1
            tmp[1][1] = tmp[1][1] + 1
            continue
        if int(row[3]) >= 3 and int(row[3]) <= 5:
            if row[-1] != 'null':
                tmp[2][0] = tmp[2][0] + 1
            tmp[2][1] = tmp[2][1] + 1
            continue
        if int(row[3]) >= 6 and int(row[3]) <= 10:
            if row[-1] != 'null':
                tmp[3][0] = tmp[3][0] + 1
            tmp[3][1] = tmp[3][1] + 1
    user_use_coupon_according_distance_record[key] = tmp
for key in user_use_coupon_according_distance_record:
    record = user_use_coupon_according_distance_record[key]
    tmp = []
    for i in range(5):
        tmp.append(record[i])
    user_use_coupon_according_distance_record[key] = tmp
# store pickle
f = file('../../ccf_data/statistic_analysis/user_use_coupon_according_distance_record.pkl','wb')
pickle.dump(user_use_coupon_according_distance_record,f)
f.close()
user_use_coupon_according_distance_record = {}
# ---------- 用户每种满x减y的优惠券的使用情况 --------
user_coupon_XtoY_use_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if not user_coupon_XtoY_use_record.has_key(line[0]):
        user_coupon_XtoY_use_record[line[0]] = {}
    if line[2] == 'null':
        continue
    if len(line[3].split(':')) == 1:
        continue
    if not user_coupon_XtoY_use_record[line[0]].has_key(line[3]):
        user_coupon_XtoY_use_record[line[0]][line[3]] = [0,0]
    if line[-1] != 'null':
        user_coupon_XtoY_use_record[line[0]][line[3]][0] = user_coupon_XtoY_use_record[line[0]][line[3]][0] + 1
    user_coupon_XtoY_use_record[line[0]][line[3]][1] = user_coupon_XtoY_use_record[line[0]][line[3]][1] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/user_coupon_XtoY_use_record.pkl','wb')
pickle.dump(user_coupon_XtoY_use_record,f)
f.close()
user_coupon_XtoY_use_record = {}
# ---------- 用户每种折扣的优惠券的使用情况 --------
user_coupon_discount_use_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if not user_coupon_discount_use_record.has_key(line[0]):
        user_coupon_discount_use_record[line[0]] = {}
    if line[2] == 'null':
        continue
    if len(line[3].split(':')) == 2:
        continue
    if not user_coupon_discount_use_record[line[0]].has_key(line[3]):
        user_coupon_discount_use_record[line[0]][line[3]] = [0,0]
    if line[-1] != 'null':
        user_coupon_discount_use_record[line[0]][line[3]][0] = user_coupon_discount_use_record[line[0]][line[3]][0] + 1
    user_coupon_discount_use_record[line[0]][line[3]][1] = user_coupon_discount_use_record[line[0]][line[3]][1] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/user_coupon_discount_use_record.pkl','wb')
pickle.dump(user_coupon_discount_use_record,f)
f.close()
user_coupon_discount_use_record = {}
# ---------- 商店每种满x减y的优惠券的使用情况 --------
merchant_coupon_XtoY_use_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if not merchant_coupon_XtoY_use_record.has_key(line[1]):
        merchant_coupon_XtoY_use_record[line[1]] = {}
    if line[2] == 'null':
        continue
    if len(line[3].split(':')) == 1:
        continue
    if not merchant_coupon_XtoY_use_record[line[1]].has_key(line[3]):
        merchant_coupon_XtoY_use_record[line[1]][line[3]] = [0,0]
    if line[-1] != 'null':
        merchant_coupon_XtoY_use_record[line[1]][line[3]][0] = merchant_coupon_XtoY_use_record[line[1]][line[3]][0] + 1
    merchant_coupon_XtoY_use_record[line[1]][line[3]][1] = merchant_coupon_XtoY_use_record[line[1]][line[3]][1] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_coupon_XtoY_use_record.pkl','wb')
pickle.dump(merchant_coupon_XtoY_use_record,f)
f.close()
merchant_coupon_XtoY_use_record = {}
# ---------- 商店每种折扣的优惠券的使用情况 --------
merchant_coupon_discount_use_record = {}
csvfile = open('../../ccf_data/cv_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if not merchant_coupon_discount_use_record.has_key(line[1]):
        merchant_coupon_discount_use_record[line[1]] = {}
    if line[2] == 'null':
        continue
    if len(line[3].split(':')) == 2:
        continue
    if not merchant_coupon_discount_use_record[line[1]].has_key(line[3]):
        merchant_coupon_discount_use_record[line[1]][line[3]] = [0,0]
    if line[-1] != 'null':
        merchant_coupon_discount_use_record[line[1]][line[3]][0] = merchant_coupon_discount_use_record[line[1]][line[3]][0] + 1
    merchant_coupon_discount_use_record[line[1]][line[3]][1] = merchant_coupon_discount_use_record[line[1]][line[3]][1] + 1
# store pickle
f = file('../../ccf_data/statistic_analysis/merchant_coupon_discount_use_record.pkl','wb')
pickle.dump(merchant_coupon_discount_use_record,f)
f.close()
merchant_coupon_discount_use_record = {}
'''


















