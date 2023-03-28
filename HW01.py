# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 20:24:18 2023

@author: USER
"""

scores = [100,60,70,80,99,100,66]

n = int(input('請輸入分數:'))
    
    if scores.count(n) > 0:
        index = scores.index(n)
        scores.pop(index)
        print(scores)
    
    elif scores.count(n) == 0:
        print('找不到')