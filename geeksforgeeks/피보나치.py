# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:02:42 2019

@author: kist1
"""
#%%
def fibo(n): 
    if n < 2: return(n)
    else : return(fibo(n-1) + fibo(n-2))
    
fibo(1)
fibo(2)
fibo(3)
fibo(4)
fibo(35)
#%%
memo = {1:1, 2:1}
def fibo(n):
    if n not in memo:
        memo[n] = fibo(n-1) + fibo(n-2)
    return(memo[n])

fibo(1)
fibo(2)
fibo(3)
fibo(35) 
#%%
def fibo(n):
    a, b = 1, 0
    for _ in range(n):
        a, b = b, a+b
    return(b)

fibo(1)
fibo(2)
fibo(3)
fibo(35)
