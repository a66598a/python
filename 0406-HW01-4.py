# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 15:18:16 2023

@author: user
"""

list1 = []
list2 = []
count = 0
while True:
    num1 = int(input('中獎號碼:'))
        
    if list1.count(num1) == 0:
        if num1 >= 1 and num1 <=49:
            list1.append(num1)
            print(list1)
            
    if len(list1) > 5:
        break
        
print()
        
while True:
    num2 = int(input('抽獎號碼:'))
        
    if list2.count(num2) == 0:
        if num2 >= 1 and num2 <=49:
            list2.append(num2)
            print(list2)

    if len(list2) > 5:
        break

print()
        
for m in range(len(list1)):
    for c in range(len(list2)):
        if list1[m] == list2[c]: #雙圈迴圈判斷list1[0] == list2[所引值]
            count += 1
print('中了',count,'注')