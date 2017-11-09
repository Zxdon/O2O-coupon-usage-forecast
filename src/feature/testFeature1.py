# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:17:30 2016

@author: zhuxiaodong
"""

import csv
import pickle

'''
user_consume_record = pickle.load(open('../../ccf_data/statistic_analysis/user_consume_record.pkl','rb'))
user_use_coupon_date_record = pickle.load(open('../../ccf_data/statistic_analysis/user_use_coupon_date_record.pkl','rb'))
merchant_consume_record = pickle.load(open('../../ccf_data/statistic_analysis/merchant_consume_record.pkl','rb'))
merchant_user_consume_number_record = pickle.load(open('../../ccf_data/statistic_analysis/merchant_user_consume_number_record.pkl','rb'))
user_merchant_record = pickle.load(open('../../ccf_data/statistic_analysis/user_merchant_record.pkl','rb'))
coupon_distance_record = pickle.load(open('../../ccf_data/statistic_analysis/coupon_distance_record.pkl','rb'))
user_use_coupon_according_distance_record = pickle.load(open('../../ccf_data/statistic_analysis/user_use_coupon_according_distance_record.pkl','rb'))
XtoYcategory_use_record = pickle.load(open('../../ccf_data/statistic_analysis/XtoYcategory_use_record.pkl','rb'))
discountCategory_use_record = pickle.load(open('../../ccf_data/statistic_analysis/discountCategory_use_record.pkl','rb'))
user_coupon_XtoY_use_record = pickle.load(open('../../ccf_data/statistic_analysis/user_coupon_XtoY_use_record.pkl','rb'))
user_coupon_discount_use_record = pickle.load(open('../../ccf_data/statistic_analysis/user_coupon_discount_use_record.pkl','rb'))
merchant_coupon_XtoY_use_record = pickle.load(open('../../ccf_data/statistic_analysis/merchant_coupon_XtoY_use_record.pkl','rb'))
merchant_coupon_discount_use_record = pickle.load(open('../../ccf_data/statistic_analysis/merchant_coupon_discount_use_record.pkl','rb'))
XtoYcategory_index = pickle.load(open('../../ccf_data/statistic_analysis/XtoYcategory_index.pkl','rb'))
discountCategory_index = pickle.load(open('../../ccf_data/statistic_analysis/discountCategory_index.pkl','rb'))
'''
user_consume_record = pickle.load(open('../../ccf_data/statistic_analysis/user_consume_record.pkl','rb'))
user_use_coupon_date_record = pickle.load(open('../../ccf_data/statistic_analysis/user_use_coupon_date_record.pkl','rb'))
merchant_consume_record = pickle.load(open('../../ccf_data/statistic_analysis/merchant_consume_record.pkl','rb'))
merchant_user_consume_number_record = pickle.load(open('../../ccf_data/statistic_analysis/merchant_user_consume_number_record.pkl','rb'))
user_merchant_record = pickle.load(open('../../ccf_data/statistic_analysis/user_merchant_record.pkl','rb'))
coupon_distance_record = pickle.load(open('../../ccf_data/statistic_analysis/coupon_distance_record.pkl','rb'))
user_use_coupon_according_distance_record = pickle.load(open('../../ccf_data/statistic_analysis/user_use_coupon_according_distance_record.pkl','rb'))

test_data = []
csvfile = open('../../ccf_data/original_data/ccf_offline_stage1_test.csv','rU')
lines = csv.reader(csvfile)
for line in lines:
    record = []
    record.extend(line)
    
    '''
    #1. 用户普通消费的数量
    #2. 用户使用优惠券的数量
    #3. 用户未使用优惠券的数量    
    if user_consume_record.has_key(line[0]):
        record.extend(user_consume_record[line[0]])
    else:
        record.extend([0,0,0])
    '''
    #2. 用户使用优惠券的数量
    if user_consume_record.has_key(line[0]):
        record.extend([user_consume_record[line[0]][1]])
    else:
        record.extend([0])
   
    #4. 用户对优惠券的使用率
    if user_consume_record.has_key(line[0]):
        coupon_num = user_consume_record[line[0]][1] + user_consume_record[line[0]][2]
        if coupon_num > 0:
            record.extend([user_consume_record[line[0]][1]*1.0/coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    #5. 用户普通消费和使用优惠券的比例（用户使用优惠券占总消费的比例）
    if user_consume_record.has_key(line[0]):
        coupon_num = user_consume_record[line[0]][0] + user_consume_record[line[0]][1]
        if coupon_num > 0:
            record.extend([user_consume_record[line[0]][1]*1.0/coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    #6. 用户使用优惠券在15日之内占总使用优惠券的比例
    if user_use_coupon_date_record.has_key(line[0]):
        coupon_num = user_use_coupon_date_record[line[0]][-1]
        if coupon_num > 0:
            record.extend([user_use_coupon_date_record[line[0]][3]*1.0/coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    #7. 该商店的用户普通消费次数
    #8. 商店使用优惠券的次数
    #9. 商店未使用优惠券的次数
    if merchant_consume_record.has_key(line[1]):
        record.extend(merchant_consume_record[line[1]])
    else:
        record.extend([0,0,0])
    '''
    #7. 该商店的用户普通消费次数
    #8. 商店使用优惠券的次数
    if merchant_consume_record.has_key(line[1]):
        record.extend(merchant_consume_record[line[1]][:2])
    else:
        record.extend([0,0])

    #10. 商店优惠券使用率
    if merchant_consume_record.has_key(line[1]):
        coupon_num = merchant_consume_record[line[1]][1] + merchant_consume_record[line[1]][2]
        if coupon_num > 0:
            record.extend([merchant_consume_record[line[1]][1]*1.0/coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])

    #11. 使用优惠券占总消费的比例
    if merchant_consume_record.has_key(line[1]):
        coupon_num = merchant_consume_record[line[1]][0] + merchant_consume_record[line[1]][1]
        if coupon_num > 0:
            record.extend([merchant_consume_record[line[1]][1]*1.0/coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    #12. 该商店的回头客比例
    if merchant_user_consume_number_record.has_key(line[1]):
        people_num = len(merchant_user_consume_number_record[line[1]][0]) + len(merchant_user_consume_number_record[line[1]][1])
        if people_num > 0:
            record.extend([len(merchant_user_consume_number_record[line[1]][1])*1.0/people_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    #13. 用户对该商店的普通消费的次数
    #14. 用户在该商店使用优惠券的次数
    if user_merchant_record.has_key(line[0]):
        if user_merchant_record[line[0]].has_key(line[1]):   
            record.extend(user_merchant_record[line[0]][line[1]][:2])
        else:
            record.extend([0,0])
    else:
        record.extend([0,0])
    '''
    #15. 用户在该商店使用优惠券的次数/总消费次数
    if user_merchant_record.has_key(line[0]):
        if user_merchant_record[line[0]].has_key(line[1]): 
            consume_num = user_merchant_record[line[0]][line[1]][0] + user_merchant_record[line[0]][line[1]][1]
            if consume_num > 0:      
                record.extend([user_merchant_record[line[0]][line[1]][1]*1.0/consume_num])
            else:
                record.extend([0.0])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    #16. 用户在该商店使用优惠券的次数/领取优惠券的次数
    if user_merchant_record.has_key(line[0]):
        if user_merchant_record[line[0]].has_key(line[1]): 
            coupon_num = user_merchant_record[line[0]][line[1]][1] + user_merchant_record[line[0]][line[1]][2]
            if coupon_num > 0:      
                record.extend([user_merchant_record[line[0]][line[1]][1]*1.0/coupon_num])
            else:
                record.extend([0.0])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    #17. 用户对该商店的惠顾率
    if user_merchant_record.has_key(line[0]):
        merchant_record = user_merchant_record[line[0]]
        total_consume_num = 0
        for key in merchant_record:
            total_consume_num = total_consume_num + merchant_record[key][0] + merchant_record[key][1]
        if merchant_record.has_key(line[1]):
            if total_consume_num > 0:
                record.extend([(merchant_record[line[1]][0] + merchant_record[line[1]][1])*1.0/total_consume_num])
            else:
                record.extend([0.0])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    
    #18. 用户是否光顾过该商店(0/1)
    if merchant_user_consume_number_record.has_key(line[1]):
        if (line[0] in merchant_user_consume_number_record[line[1]][0]) or (line[0] in merchant_user_consume_number_record[line[1]][1]):
            record.extend([1])
        else:
            record.extend([0])
    else:
        record.extend([0])     
    #19. 用户是否是该商店的回头客(0/1)
    if merchant_user_consume_number_record.has_key(line[1]):
        if (line[0] in merchant_user_consume_number_record[line[1]][1]):
            record.extend([1])
        else:
            record.extend([0])
    else:
        record.extend([0]) 
    
    #20. 用户对该商店的距离
    if line[4] == 'null':
        record.extend([5])
    else:
        record.extend([int(line[4])])
    '''
    #21. 该优惠券的种类 (0表示折扣率，1表示满x减y)
    if len(line[3].split(':')) == 2:
        record.extend([1])
    else:
        record.extend([0])
    #22. 该优惠券满x (若为折扣率，则为0)
    if len(line[3].split(':')) == 2:
        record.extend([int(line[3].split(':')[0])])
    else:
        record.extend([0])
    #23. 该优惠券减y (若为折扣率，则为0)
    if len(line[3].split(':')) == 2:
        record.extend([int(line[3].split(':')[1])])
    else:
        record.extend([0])
    #24. 该优惠券折扣率 (若为满x减y，则为0)
    if len(line[3].split(':')) == 1:
        record.extend([float(line[3])])
    else:
        record.extend([0])
    '''
    #25. 根据距离优惠券的使用比例
    record.extend([coupon_distance_record[line[4]][0]*1.0/coupon_distance_record[line[4]][1]])
    #26. 用户根据距离优惠券的使用情况 使用比例
    if user_use_coupon_according_distance_record.has_key(line[0]):
        distance_record = user_use_coupon_according_distance_record[line[0]]
        if line[4] == 'null':
            index = 4
        if line[4] != 'null':
            if int(line[4]) == 0:
                index = 0
            if int(line[4]) >= 1 and int(line[4]) <= 2:
                index = 1
            if int(line[4]) >= 3 and int(line[4]) <= 5:
                index = 2
            if int(line[4]) >= 6 and int(line[4]) <= 10:
                index = 3
        tmp = distance_record[index]
        if tmp[1] > 0:
            record.extend([tmp[0]*1.0/tmp[1]])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    #27. 满x减y的优惠券使用比例
    if XtoYcategory_use_record.has_key(line[3]):
        record.extend([XtoYcategory_use_record[line[3]][0]*1.0/XtoYcategory_use_record[line[3]][1]])
    else:
        record.extend([0.0])
    #28. 折扣优惠券使用比例 discountCategory_use_record
    if discountCategory_use_record.has_key(line[3]):
        record.extend([discountCategory_use_record[line[3]][0]*1.0/discountCategory_use_record[line[3]][1]])
    else:
        record.extend([0.0]) 
    #29. 用户是否用过满x减y的优惠券
    user_XtoY_coupon_num = 0
    if user_coupon_XtoY_use_record.has_key(line[0]):
        use_record = user_coupon_XtoY_use_record[line[0]]
        for coupon_category in use_record:
            user_XtoY_coupon_num = user_XtoY_coupon_num + use_record[coupon_category][0]
        if user_XtoY_coupon_num > 0:
            record.extend([1])
        else:
            record.extend([0])
    else:
        record.extend([0])
    #30. 用户是否用过折扣优惠券 user_coupon_discount_use_record
    user_discount_coupon_num = 0
    if user_coupon_discount_use_record.has_key(line[0]):
        use_record = user_coupon_discount_use_record[line[0]]
        for coupon_category in use_record:
            user_discount_coupon_num = user_discount_coupon_num + use_record[coupon_category][0]
        if user_discount_coupon_num > 0:
            record.extend([1])
        else:
            record.extend([0])
    else:
        record.extend([0])
    #31. 用户对于满x减y的优惠券类型的使用比例
    user_use_XtoY_coupon_num = 0
    user_XtoY_coupon_num = 0
    if user_coupon_XtoY_use_record.has_key(line[0]):
        use_record = user_coupon_XtoY_use_record[line[0]]
        for coupon_category in use_record:            
            user_use_XtoY_coupon_num = user_use_XtoY_coupon_num + use_record[coupon_category][0]
            user_XtoY_coupon_num = user_XtoY_coupon_num + use_record[coupon_category][1]
        if user_XtoY_coupon_num > 0:
            record.extend([user_use_XtoY_coupon_num*1.0/user_XtoY_coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    #32. 用户对于折扣优惠券类型的使用比例
    user_use_discount_coupon_num = 0
    user_discount_coupon_num = 0
    if user_coupon_discount_use_record.has_key(line[0]):
        use_record = user_coupon_discount_use_record[line[0]]
        for coupon_category in use_record:
            user_use_discount_coupon_num = user_use_discount_coupon_num + use_record[coupon_category][0]
            user_discount_coupon_num = user_discount_coupon_num + use_record[coupon_category][1]
        if user_discount_coupon_num > 0:
            record.extend([user_use_discount_coupon_num*1.0/user_discount_coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    '''
    #33. 用户对于满x减y的优惠券类型分类  每一类的使用比例
    info = [0.0] * 36
    if user_coupon_XtoY_use_record.has_key(line[0]):
        user_record = user_coupon_XtoY_use_record[line[0]]
        for key in user_record:
            index = XtoYcategory_index[key]
            use_ratio = 0.0
            if user_record[key][1] > 0:
                use_ratio = user_record[key][0]*1.0/user_record[key][1]
            info[index] = use_ratio
    record.extend(info)
    #34. 用户对于折扣优惠券类型分类 每一类的使用比例
    info = [0.0] * 9
    if user_coupon_discount_use_record.has_key(line[0]):
        user_record = user_coupon_discount_use_record[line[0]]
        for key in user_record:
            index = discountCategory_index[key]
            use_ratio = 0.0
            if user_record[key][1] > 0:
                use_ratio = user_record[key][0]*1.0/user_record[key][1]
            info[index] = use_ratio
    record.extend(info)    
    '''
    '''
    #35. 该商店是否发过满x减y的优惠券
    merchant_XtoY_coupon_num = 0
    if merchant_coupon_XtoY_use_record.has_key(line[1]):
        use_record = merchant_coupon_XtoY_use_record[line[1]]
        for coupon_category in use_record:
            merchant_XtoY_coupon_num = merchant_XtoY_coupon_num + use_record[coupon_category][0]
        if merchant_XtoY_coupon_num > 0:
            record.extend([1])
        else:
            record.extend([0])
    else:
        record.extend([0])
    #36. 该商店是否发过折扣优惠券
    merchant_discount_coupon_num = 0
    if merchant_coupon_discount_use_record.has_key(line[1]):
        use_record = merchant_coupon_discount_use_record[line[1]]
        for coupon_category in use_record:
            merchant_discount_coupon_num = merchant_discount_coupon_num + use_record[coupon_category][0]
        if merchant_discount_coupon_num > 0:
            record.extend([1])
        else:
            record.extend([0])
    else:
        record.extend([0])
    #37. 商店满x减y类型的消费券的使用比例
    merchant_use_XtoY_coupon_num = 0
    merchant_XtoY_coupon_num = 0
    if merchant_coupon_XtoY_use_record.has_key(line[1]):
        use_record = merchant_coupon_XtoY_use_record[line[1]]
        for coupon_category in use_record:            
            merchant_use_XtoY_coupon_num = merchant_use_XtoY_coupon_num + use_record[coupon_category][0]
            merchant_XtoY_coupon_num = merchant_XtoY_coupon_num + use_record[coupon_category][1]
        if merchant_XtoY_coupon_num > 0:
            record.extend([merchant_use_XtoY_coupon_num*1.0/merchant_XtoY_coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    #38. 商店折扣优惠券是使用比例
    merchant_use_discount_coupon_num = 0
    merchant_discount_coupon_num = 0
    if merchant_coupon_discount_use_record.has_key(line[1]):
        use_record = merchant_coupon_discount_use_record[line[1]]
        for coupon_category in use_record:
            merchant_use_discount_coupon_num = merchant_use_discount_coupon_num + use_record[coupon_category][0]
            merchant_discount_coupon_num = merchant_discount_coupon_num + use_record[coupon_category][1]
        if merchant_discount_coupon_num > 0:
            record.extend([merchant_use_discount_coupon_num*1.0/merchant_discount_coupon_num])
        else:
            record.extend([0.0])
    else:
        record.extend([0.0])
    '''
    '''
    #39. 商店每一种满x减y类型的消费券的使用比例
    info = [0.0] * 36
    if merchant_coupon_XtoY_use_record.has_key(line[0]):
        merchant_record = merchant_coupon_XtoY_use_record[line[0]]
        for key in merchant_record:
            index = XtoYcategory_index[key]
            use_ratio = 0.0
            if merchant_record[key][1] > 0:
                use_ratio = merchant_record[key][0]*1.0/merchant_record[key][1]
            info[index] = use_ratio
    record.extend(info)
    #40. 商店每一种折扣优惠券是使用比例
    info = [0.0] * 9
    if merchant_coupon_discount_use_record.has_key(line[0]):
        merchant_record = merchant_coupon_discount_use_record[line[0]]
        for key in merchant_record:
            index = discountCategory_index[key]
            use_ratio = 0.0
            if merchant_record[key][1] > 0:
                use_ratio = merchant_record[key][0]*1.0/merchant_record[key][1]
            info[index] = use_ratio
    record.extend(info)    
    '''
    # --------------------------------------------------------------

    test_data.append(record)
csvfile.close()

user_consume_record = {}
user_use_coupon_date_record = {}
merchant_consume_record = {}
merchant_user_consume_number_record = {}
user_merchant_record = {}
coupon_distance_record = {}
user_use_coupon_according_distance_record = {}
XtoYcategory_use_record = {}
discountCategory_use_record = {}
user_coupon_XtoY_use_record = {}
user_coupon_discount_use_record = {}
merchant_coupon_XtoY_use_record = {}
merchant_coupon_discount_use_record = {}

# store pickle
f = file('../../ccf_data/feature/test_data1.pkl','wb')
pickle.dump(test_data,f)
f.close()






























