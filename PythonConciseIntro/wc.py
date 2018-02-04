# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:45:14 2018

@author: TrungNT
"""

import sys
infile = open(sys.argv[1])
dic = {}
for line in infile:
    for word in line.split():
        word = word.lower().strip("'?,.;!-/\"")
        if word not in dic:
            dic[word] = 0
        dic[word] += 1
infile.close()

keys = sorted(dic)
"""for key in keys:
    print(key,dic[key])
"""
for key in dic.keys():
    print(key,dic[key])
            