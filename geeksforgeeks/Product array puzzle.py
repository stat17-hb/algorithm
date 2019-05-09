# https://practice.geeksforgeeks.org/problems/product-array-puzzle/0

#%%

import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    P = ""
    prod = 1
    for k in A:
        prod = prod*k
    for i in range(N):
        if i == 0: P = P + str(int(prod/A[i]))
        else : P = P + " " + str(int(prod/A[i]))
    print(P)
    
