# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 23:31:25 2018

@author: TrungNT
"""

import sys
src = sys.argv[1]
dest = sys.argv[2]

srcFile = open(sys.argv[1])
destFile = open(sys.argv[2],"w")

for line in srcFile:
    destFile.write(line)

srcFile.close();
destFile.close();