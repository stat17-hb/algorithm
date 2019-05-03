# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:35:52 2019

@author: kist1
"""

#%%
dim = ()
mat = []
f = open("D:/OneDrive - 고려대학교/석사/알고리즘/ex1.txt", "r")
lines = f.readlines()
temp = []
for i in range(len(lines)):
    temp.append(lines[i].split("\n"))
f.close
temp
#%%
for i in range(len(lines)):
    if i==0: dim = lines[i].split(" ")
    else: mat.append(lines[i].split("\n")[0])
dim
mat