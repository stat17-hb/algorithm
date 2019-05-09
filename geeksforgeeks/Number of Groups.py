import os
import sys
from itertools import combinations

os.chdir("E:/OneDrive - 고려대학교/석사/알고리즘")
sys.stdin = open("number_of_groups.txt", "r")

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    all2comb = list(combinations(arr, 2))
    all3comb = list(combinations(arr, 3))
    sum_all2comb = list(map(sum, all2comb))
    sum_all3comb = list(map(sum, all3comb))
    
    count=0
    for i in sum_all2comb:
        if i % 3==0 : count += 1
    for j in sum_all3comb:
        if j % 3==0 : count += 1
    print(count)