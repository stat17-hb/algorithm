# https://practice.geeksforgeeks.org/problems/finding-position/0

#%%
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    queue = [i+1 for i in range(N)]
    while len(queue)!=1:
        queue = [queue[i] for i in range(len(queue)) if (i+1) % 2 ==0]
    print(queue[0])