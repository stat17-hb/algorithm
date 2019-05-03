# -*- coding: utf-8 -*-
#%%
# 데이터 읽기
import os
import sys

os.getcwd()
os.chdir("E:/OneDrive - 고려대학교/석사/알고리즘")
sys.stdin = open("ex6.txt", "r")
dim = list(map(int, sys.stdin.readline().split()))
nrow = dim[0]
ncol = dim[1]
X = []
for _ in range(nrow):
    X.append(list(map(int, sys.stdin.readline().split())))
sys.stdin.close()
#%%
# 바이러스 위치 확인
virus_set = set()
for row in range(nrow):
    for col in range(ncol):
        if X[row][col]==2: virus_set.add((row, col)) 
#virus_set

#%%
# 벽을 세울 위치 확인
zero_set = set()
for row in range(nrow):
    for col in range(ncol):
        if X[row][col]==0: zero_set.add((row, col)) 
#zero_set

#%%
# 벽을 세울 위치의 모든 조합
from itertools import combinations
zero_comb = list(combinations(zero_set,3))
#zero_comb

#%%
# 바이러스 전파
from collections import deque
def spread(X, i, j, virus_set):
    if X[i][j]==2:
        if i==0 and j==0:
            if X[i][j+1]==0:# 오른쪽
                X[i][j+1]=2 
                virus_set.append((i, j+1)) 
            if X[i+1][j]==0: # 아래
                X[i+1][j]=2 
                virus_set.append((i+1, j))
            
        elif i==0 and j==(ncol-1):
            if X[i][j-1]==0: # 왼쪽
                X[i][j-1]=2
                virus_set.append((i, j-1))
            if X[i+1][j]==0: # 아래
                X[i+1][j]=2 
                virus_set.append((i+1, j))
            
        elif i==(nrow-1) and j==0:
            if X[i][j+1]==0: 
                X[i][j+1]=2 # 오른쪽
                virus_set.append((i, j+1)) 
            if X[i-1][j]==0: 
                X[i-1][j]=2 # 위
                virus_set.append((i-1, j))
            
        elif i==(nrow-1) and j==(ncol-1):
            if X[i][j-1]==0: 
                X[i][j-1]=2 # 왼쪽
                virus_set.append((i, j-1))
            if X[i-1][j]==0: 
                X[i-1][j]=2 # 위
                virus_set.append((i-1, j))
            
        elif i==0 and j not in [0, ncol-1]:
            if X[i+1][j]==0: 
                X[i+1][j]=2 # 아래
                virus_set.append((i+1, j))
            if X[i][j-1]==0: 
                X[i][j-1]=2 # 왼쪽
                virus_set.append((i, j-1))
            if X[i][j+1]==0: 
                X[i][j+1]=2 # 오른쪽
                virus_set.append((i, j+1))
            
        elif i==(nrow-1) and j not in [0, ncol-1]:
            if X[i][j-1]==0: 
                X[i][j-1]=2 # 왼쪽
                virus_set.append((i, j-1))
            if X[i][j+1]==0: 
                X[i][j+1]=2 # 오른쪽
                virus_set.append((i, j+1))
            if X[i-1][j]==0: 
                X[i-1][j]=2 # 위
                virus_set.append((i-1, j))
       
        elif i not in [0, nrow-1] and j==0:
            if X[i][j+1]==0: 
                X[i][j+1]=2 # 오른쪽
                virus_set.append((i, j+1))
            if X[i-1][j]==0: 
                X[i-1][j]=2 # 위
                virus_set.append((i-1, j))
            if X[i+1][j]==0: 
                X[i+1][j]=2 # 아래
                virus_set.append((i+1, j))
            
        elif i not in [0, nrow-1] and j==(ncol-1):
            if X[i][j-1]==0: 
                X[i][j-1]=2 # 왼쪽
                virus_set.append((i, j-1))
            if X[i+1][j]==0: 
                X[i+1][j]=2 # 아래
                virus_set.append((i+1, j))
            if X[i-1][j]==0: 
                X[i-1][j]=2 # 위
                virus_set.append((i-1, j))
            
        else :
            if X[i][j+1]==0: 
                X[i][j+1]=2 # 오른쪽
                virus_set.append((i, j+1))
            if X[i][j-1]==0: 
                X[i][j-1]=2 # 왼쪽
                virus_set.append((i, j-1))
            if X[i+1][j]==0: 
                X[i+1][j]=2 # 아래
                virus_set.append((i+1, j))
            if X[i-1][j]==0: 
                X[i-1][j]=2 # 위
                virus_set.append((i-1, j))
    else : pass    
    return(X)

def spread_virus(X, virus_set):
    virus_set_temp = deque(virus_set.copy())
    while len(virus_set_temp)!=0:
        idx = virus_set_temp.popleft()
        spread(X, idx[0], idx[1], virus_set_temp)
        #print("index: ", idx,"virus_set: ", virus_set_temp)
    return(X)

#%%
# 벽 세우기
def build_wall(X, comb_idx):
    for point in range(3):
        row_idx = zero_comb[comb_idx][point][0]
        col_idx = zero_comb[comb_idx][point][1]
        X[row_idx][col_idx] = 1
    return(X)

#%%
# 0의 개수 세기
def count_zero(X, nrow, ncol):
    count = 0
    for row in range(nrow):
        for col in range(ncol):
            if X[row][col]==0: count += 1
    return(count)
    
#%%
num_comb = len(zero_comb)
count_list = []
for comb_idx in range(num_comb):
    X_new = [element.copy() for element in X]
    build_wall(X_new, comb_idx)
    spread_virus(X_new, virus_set)
    count_list.append(count_zero(X_new, nrow, ncol))
#count_list.index(max(count_list))
#%%
# 최대 크기 출력
max(count_list)
# zero_comb[count_list.index(max(count_list))]