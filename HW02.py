# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 21:01:41 2023

@author: USER
"""
num = list()

for i in range(0,6):
    n = int(input('請輸入數字:'))
    num.append(n)

y = sorted(num,reverse=True)

print(num)
print(y)