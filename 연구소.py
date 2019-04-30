# 데이터 읽기
import sys
from collections import deque
from itertools import combinations

nrow, ncol = list(map(int, sys.stdin.readline().split()))
X = []
for _ in range(nrow):
    X.append(list(map(int, sys.stdin.readline().split())))

# 바이러스 위치 확인
virus_set = set()
for row in range(nrow):
    for col in range(ncol):
        if X[row][col]==2: virus_set.add((row, col))

# 벽을 세울 위치 확인
zero_set = set()
for row in range(nrow):
    for col in range(ncol):
        if X[row][col]==0: zero_set.add((row, col)) 

# 벽을 세울 위치의 모든 조합
zero_comb = list(combinations(zero_set,3))

# 바이러스 전파
def visit(X, row, col, nrow, ncol, virus_set):
    all_direction = [(-1,0),(1,0),(0,1),(0,-1)]
    if X[row][col]==2:
        for drow, dcol in all_direction:
            if row+drow == -1 or row+drow== nrow or col+dcol==-1 or col+dcol==ncol: pass
            elif X[row+drow][col+dcol]==0:
                X[row+drow][col+dcol] = 2
                virus_set.append((row+drow, col+dcol))
    return(X)

def spread_virus(X, nrow, ncol, virus_set):
    virus_set_temp = deque(virus_set.copy())
    while True:
        if len(virus_set_temp)==0: break
        row, col = virus_set_temp.popleft()
        visit(X, row, col, nrow, ncol, virus_set_temp)
    return(X)

# 벽 세우기
def build_wall(X, zero_comb, comb_idx):
    for row, col in zero_comb[comb_idx]:
        X[row][col] = 1
    return(X)

# 0의 개수 세기
def count_zero(X, nrow, ncol):
    count = 0
    for row in range(nrow):
        for col in range(ncol):
            if X[row][col]==0: count += 1
    return(count)
    
if __name__=='__main__':
    safezone_size_list = []
    for comb_idx in range(len(zero_comb)):
        X_new = [element.copy() for element in X]
        build_wall(X_new, zero_comb, comb_idx)
        spread_virus(X_new, nrow, ncol, virus_set)
        safezone_size_list.append(count_zero(X_new, nrow, ncol))
    print(max(safezone_size_list))
