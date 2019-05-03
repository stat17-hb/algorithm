#%%
# 데이터 읽기
import os
import sys

os.chdir("E:/OneDrive - 고려대학교/석사/알고리즘/퇴사")
sys.stdin = open("ex5.txt", "r")
N = int(sys.stdin.readline())
T, P = [], []
for _ in range(N):
    X = list(map(int, sys.stdin.readline().split()))
    T.append(X[0])
    P.append(X[1])
sys.stdin.close()

memo = {} # 값을 저장할 딕셔너리
max_idx_out = max([i+T[i] for i in range(N) if i+T[i] >=N])

# index 범위를 벗어날 수 있는 후보를 모두 찾고 딕셔너리에 값을 0으로 저장
if N==max_idx_out: 
    memo[N] = 0
else: 
    for i in range(N, max(N, max_idx_out)): memo[i] = 0

def f(i):
    if i>N-1 : pass # 인덱스 범위를 벗어나는 값이 들어오면 딕셔너리에 이미 맵핑되어 있는 0을 리턴
    elif i+T[i]>N: memo[i] = f(i+1) # 퇴사 전에 상담을 완료할 수 없으면 다음 날로 넘어감
    else : memo[i] = max(P[i]+f(i+T[i]), f(i+1)) # i번째 날의 상담을 맡았을 때 수익과 i+1번째 날의 상담을 맡았을 때 수익을 비교하여 더 큰 쪽을 선택
    return(memo[i])

print(max([f(i) for i in range(N)]))