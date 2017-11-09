# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:45:05 2016

@author: zhuxiaodong

从原始的统计信息中，直接分割训练和验证集，这样可以使得训练和验证集的分布不同，而
验证集和测试集的分布相同，有利于线下的测试

已知：
测试数据的由来： (1)从只发一种优惠券的,但只抽取其中一部分
               (2)发放多种优惠券的，抽取一部分
		      (3)发放多种优惠券的，但有一种优惠券被全部抽取
需要保证：
1. 不抽取普通消费的情况
2. 不能将只发一种优惠券的商店的记录全部抽取过去
3. 可以对发放多种优惠券的商店，抽取完整个优惠券的记录

valid集大概需要5000领取使用和65000领取未使用的记录
首先需要知道那些商家发放一种或多种优惠券
"""
import csv
import random
import pickle

# ------ 优惠券由那些商店发出 -----
coupon_merchant = pickle.load(open('../../ccf_data/statistic_analysis/coupon_merchant.pkl','rb'))
# ------- 商店发了那些优惠券 -------
merchant_coupon = pickle.load(open('../../ccf_data/statistic_analysis/merchant_coupon.pkl','rb'))

coupon1 = {} #完全抽取
coupon2 = {} #部分抽取
coupon3 = {} #部分抽取
# ------ 这些优惠券全部进入valid -----
# ----- 这些优惠券发放的商店，同时发放多种优惠券
count = 0
for key in coupon_merchant:
    if random.randint(0,5) < 1:
        if len(coupon_merchant[key]) != 1:
            continue
        for merchant_id in coupon_merchant[key]:
            pass
        if len(merchant_coupon[merchant_id]) > 1:
            coupon1[key] = 0
            count = count + 1
            if count >= 400:
                break

count = 0
for key in coupon_merchant:
    if random.randint(0,5) < 1 and (not coupon1.has_key(key)):
        if len(coupon_merchant[key]) != 1:
            continue
        for merchant_id in coupon_merchant[key]:
            pass
        if len(merchant_coupon[merchant_id]) > 1:
            coupon2[key] = 0
            count = count + 1
            if count >= 300:
                break

count = 0
for key in coupon_merchant:
    if random.randint(0,5) < 1 and (not coupon1.has_key(key)) and (not coupon2.has_key(key)):
        if len(coupon_merchant[key]) != 1:
            continue
        for merchant_id in coupon_merchant[key]:
            pass
        if len(merchant_coupon[merchant_id]) == 1:
            coupon3[key] = 0
            count = count + 1
            if count >= 200:
                break

ccf_offline_stage1_train = []
ccf_offline_stage1_valid = []
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_train.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    if coupon1.has_key(line[2]):
        ccf_offline_stage1_valid.append(line)
        continue
    if coupon2.has_key(line[2]):
        if random.randint(0,2) < 1:
            ccf_offline_stage1_valid.append(line)
            continue
    if coupon3.has_key(line[2]):
        if random.randint(0,2) < 1:
            ccf_offline_stage1_valid.append(line)
            continue
    ccf_offline_stage1_train.append(line)
csvfile.close()

filename = '../../ccf_data/cv_data/ccf_offline_stage1_train.csv'
csvfile = file(filename,'wb')
writer = csv.writer(csvfile)
writer.writerows(ccf_offline_stage1_train)
csvfile.close()

filename = '../../ccf_data/cv_data/ccf_offline_stage1_valid.csv'
csvfile = file(filename,'wb')
writer = csv.writer(csvfile)
writer.writerows(ccf_offline_stage1_valid)
csvfile.close()









