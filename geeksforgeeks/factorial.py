# %%
import os
import sys
os.chdir("D:/OneDrive - 고려대학교/석사/알고리즘")
sys.stdin = open("factorial.txt", "r")

N = int(sys.stdin.readline())

#%%
N=10
memo={}
def facto(n):
    if n==0: memo[n]=1
    else : memo[n]=n*facto(n-1)
    return(memo[n])

facto(N)
