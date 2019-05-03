#%%
import os
import sys
from collections import deque
from itertools import combinations

os.chdir("E:/OneDrive - 고려대학교/석사/알고리즘/치킨배달")
sys.stdin = open("ex1.txt", "r")
N, M = list(map(int, sys.stdin.readline().split()))
X = []
for _ in range(N):
    X.append(list(map(int, sys.stdin.readline().split())))
sys.stdin.close()

X
C = len(X[0])

house_set, chicken_set = set(), set()

for row in range(N):
    for col in range(N):
        if X[row][col] == 1:
            house_set.add((row, col))
        if X[row][col] == 2:
            chicken_set.add((row, col))

chicken_comb = list(combinations(chicken_set, M))

def dist(c1 , c2): return(abs(c1[0]-c2[0])+abs(c1[1]-c2[1]))

def get_min_dist(house_set, chiken_set):
    hdeq = deque(house_set)
    min_dist = []
    while len(hdeq)!=0:
        h=hdeq.popleft()
        cdeq = deque(chicken_set)
        dist_list = []
        while len(cdeq)!=0:
            c=cdeq.popleft()
            dist_list.append(dist(h,c))
        min_dist.append(min(dist_list))
    return(sum(min_dist))

cdist = []
for comb in chicken_comb:
    cdist.append(get_min_dist(house_set, comb))
print(min(cdist))



