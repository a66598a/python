# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 17:27:57 2023

@author: user
"""
count = 0
def binary_search(data, low, high, key):
    global count
    if low > high:
        count += 1
        return -1
        
    mid = int((low + high) / 2)
    
    if key == data[mid]:
        count += 1
        return mid
    
    elif key > data[mid]:
        low = mid + 1
        count += 1
        return binary_search(data, low, high, key)
        
    else:
        high = mid - 1
        count += 1
        return binary_search(data, low, high, key)   
        
print(count)    
data = [80,60,70,90,49,33,89]
data.sort()
key = 33
c = count
print(data)
ret = binary_search(data, 0, len(data)-1, key)
if ret == -1:
    print('找不到')
else:
    print('找到索引值' + str(ret),data[ret],c)


