# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 09:33:43 2018

@author: TrungNT
"""

import sys
infile = open(sys.argv[1])
outfile = open(sys.argv[2],"w")
for line in infile:
    outfile.write(str(len(line.strip("\n"))) + "\n")
infile.close()
outfile.close()