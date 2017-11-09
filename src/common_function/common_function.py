# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 22:50:19 2016

@author: zhuxiaodong

common function defined here
"""

def splitStr(str_label):
    '''
    splitStr: '12/13/45' -> [12, 13, 45]
              '/'        -> []
              '2'        -> [2]
    '''
    if str_label == '/':
        return []
    else:
        tmp = str_label.split('/')
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
    return tmp
    
def calRate(static_dict):
    '''    
    {5:1,6:1} -> {5:0.5,6:0.5}
    '''     
    sum_num = 0
    for key in static_dict:
        sum_num = sum_num + static_dict[key]
    for key in static_dict:
        static_dict[key] = round(static_dict[key]*1.0/sum_num,4)

    return static_dict
    
def dictSorted(static_dict):
    '''
    
    '''
    sortedList = sorted(static_dict.iteritems(), key=lambda d:d[1], reverse = False)    
    dictLen = len(sortedList)
    if dictLen == 0:
        return static_dict
        
    sortedIndex = []
    end = tail = 0
    while tail < dictLen:
        if (sortedList[tail][1] == sortedList[end][1]):
            tail = tail + 1
        else:
            sortedIndex.extend([tail] * (tail - end))
            end = tail
    if tail == dictLen:
        sortedIndex.extend([tail] * (tail - end))
        
    for i in range(dictLen):
        sortedIndex[i] = round(sortedIndex[i]*sortedList[i][1]*1.0/(sortedIndex[dictLen-1]*sortedList[dictLen-1][1]),4)
        
    for i in range(dictLen):
        static_dict[sortedList[i][0]] = [sortedList[i][1], sortedIndex[i]] # * sortedList[i][1]
        
    return static_dict
    
def mergeDict(dict1,dict2):
    for key in dict1:
        if dict2.has_key(key):
            dict1[key].append(dict2[key])
            
def dictToList(static_dict):
    static_list = []
    for key in static_dict:
        tmp = [key[0],key[1]]
        tmp.extend(static_dict[key])
        static_list.append(tmp)
        
    return static_list
    
#def splitList(orig_list, begin, end):
def mergeList(list1,list2):
    list_tmp = []
    length = len(list1)
    for i in range(length):
        tmp = []
        tmp.extend(list1[i])
        tmp.append(list2[i])
        list_tmp.append(tmp)
    return list_tmp
    
def gen_result(filename,data):
    import csv
    filename = '../../bytecup2016data/result/' + filename
    csvfile = file(filename,'wb')
    writer = csv.writer(csvfile)
    writer.writerow(['qid','uid','label'])
    writer.writerows(data)
    csvfile.close()
    
def getDictKey(static_dict):
    '''    
    {5:1,6:1} -> [5,6]
    ''' 
    key_list = []
    
    for key in static_dict:
        key_list.append(key)
        
    return key_list
    
def randomList(static_list, rate):
    '''
    按rate比率选取list中的一部分
    '''
    result = []
    import random
    tmp = [random.random() for i in range(len(static_list))]
    for i in range(len(static_list)):
        if tmp[i] <= 0.1:
            result.append(static_list[i])
            
    return result
    
def readCsv(filename,begin = 7,label = True):
    '''
    int : 1 float: 0
    '''
    import csv
    result = []
    csvfile = open('../../ccf_data/feature/' + filename + '.csv','rU')
    lines = csv.reader(csvfile)
    for line in lines:
        tmp = []
        tmp.extend(line[:begin])
        if label:
            length = len(line) - begin -1
            for i in range(length):
                tmp.append(float(line[begin+i]))
            tmp.append(int(line[-1]))
        else:
            length = len(line) - begin
            for i in range(length):
                tmp.append(float(line[begin+i]))
        result.append(tmp)
    return result
    
def valid_submit_eval(valid_submit,test_sample_label):
    '''
    对于全0或全1的优惠券，不予测评
    将所有优惠券的auc测评出后，平均
    '''
    import numpy as np
    from sklearn.metrics import roc_curve, auc
    #先将valid_submit，test_sample_label合并
    valid_submit_label = []
    for i in range(len(valid_submit)):
        tmp = []
        tmp.extend(valid_submit[i])
        tmp.append(test_sample_label[i])
        valid_submit_label.append(tmp)
        
    #将coupon按id分开
    coupon_submit_label = {}
    for i in range(len(valid_submit_label)):
        if not coupon_submit_label.has_key(valid_submit_label[i][1]):
            coupon_submit_label[valid_submit_label[i][1]] = []
        coupon_submit_label[valid_submit_label[i][1]].append(valid_submit_label[i][-2:])
    
    count = 0
    sum_roc_auc = 0.0
    for key in coupon_submit_label:
        record = coupon_submit_label[key]
        submit = []
        label = []
        for i in range(len(record)):
            submit.append(record[i][0])
            label.append(record[i][1])
            
        if len(set(label)) <= 1:
            continue
        
        # Compute ROC curve and ROC area for each class
        fpr = dict()
        tpr = dict()
        roc_auc = dict()
        fpr, tpr, _ = roc_curve(np.array(label), np.array(submit))
        roc_auc = auc(fpr, tpr)
        sum_roc_auc = sum_roc_auc + roc_auc
        count = count + 1
    
    #print 'coupon_num:%d' %count    
    print 'avg_auc:%f' %(sum_roc_auc/count)
    
    
    
    
    
    
    
    
    
    
    