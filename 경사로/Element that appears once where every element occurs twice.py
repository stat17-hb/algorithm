# https://practice.geeksforgeeks.org/problems/element-that-appears-once-where-every-element-occurs-twice/0

#%%
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    for i in range(N):
        if A[i] not in A[:i]+A[i+1:]: print(A[i])