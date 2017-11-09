# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 10:38:22 2016

@author: zhuxiaodong

"""
import math

import csv
import pickle

def eval_function1(x):
    '''
    x >= 0
    return (1 - e^(-x))/(1 + e^x)
    '''
    return (1 - math.exp(-x))/(1 + math.exp(-x))
    
def eval_function2(x,alpha,beta):
    '''
    x>=0 
    return e^(alpha*x+beta)
    '''
    return math.exp(alpha*x + beta)
    
def cu_category(coupon_id, user_id):
    '''
    1. 验证集中有的couponid在训练集中没有出现，而且也没有人去过这家商店 返回1
    2. 验证集中有的couponid在训练集中没有出现，但有人去过这家商店 返回2
    3. 训练集和验证集中均有couponid的记录，返回3
    '''
    
    


























































