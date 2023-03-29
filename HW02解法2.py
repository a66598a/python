# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:48:17 2023

@author: user
"""

num = list()

sort1 = []

sort2 = []

for i in range(0,6):
    n = int(input('請輸入數字:'))
    num.append(n)
    sort1 = num
     
while len(sort1) > 0:
    m = min(sort1)
    sort1.remove(m)
    sort2.append(m)
    if sort2.count(m) > 1:
        index = sort2.index(m)
        sort2.remove(m)
        y = int(input('請輸入不相同之數字'))
        sort2.append(y)
        
        
print(sort2)
