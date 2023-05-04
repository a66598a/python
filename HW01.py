# -*- coding: utf-8 -*-
"""
Created on Wed May  3 19:43:26 2023

@author: user
"""
import random

sum1 = 0
list1 = []
list2 = []

for i in range(4):
    num = int(random.randint(1, 6))
    list1.append(num)

print(list1)

for i in range(1,7):
    
    if list1.count(i) == 1:
        pass
    
    elif list1.count(i) >= 2 and list1.count(i) <= 3:
        list2.append(i)
        #print(list2)

        if len(list2) == 2:
            num2 = max(list2)
            sum2 = 2 * num2
            print('點數:',sum2)
        
    elif list1.count(i) == 4:
        print('一色最大')
        
        
if len(list2) == 1:
    num1= max(list2)
    sum1 += 2 * num1
    print('點數:',sum1)

