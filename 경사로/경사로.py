#%%
import os
import sys

os.chdir("E:/OneDrive - 고려대학교/석사/알고리즘/경사로")
sys.stdin = open("ex4.txt", "r")
N, L = list(map(int, sys.stdin.readline().split()))
X = []
for _ in range(N):
    X.append(list(map(int, sys.stdin.readline().split())))
sys.stdin.close()

def is_path(path, N, L):
    for i in range(N-1):
        if abs(path[i]-path[i+1])>1 : # 내려가거나 올라갈 수 없는 경우
            return("NO")
            break
        elif path[i]-path[i+1]==-1: # 올라가야 하는 경우
            if i+1-L <0 : # 가장 바깥쪽 인덱스가 인덱스 범위를 넘어가는 경우
                return("NO")
                break
            else:
                for j in range(L-1): # i번째 셀을 포함하여 i번째 셀 뒤쪽으로 L개 셀이 같은 값인지 확인
                        if path[i] != path[i-(j+1)]: 
                            return("NO")
                            break
        elif path[i]-path[i+1]==1 : # 내려가야 하는 경우
            if i+L > N-1: # 가장 바깥쪽 인덱스가 인덱스 범위를 넘어가는 경우
                return("NO")
                break
            else : 
                for j in range(L-1): # i번째 셀 앞쪽으로 L개 셀이 같은 값인지 확인
                    if path[i+1] != path[i+1+(j+1)]: 
                        return("NO")
                        break
                # 만약 i 다음 인덱스에서 올라가는 경우가 생기면
                if -1 in [path[l]-path[l+1] for l in range(i, N-1)]:
                    # 내려갔다 올라갈때 경사로가 겹치지 못하게
                    for k in range(L):
                        if i+(L+k+1) > N-1: # 인덱스 범위를 넘어가는 경우
                            return("NO")
                            break
                        elif path[i]==path[i+(L+k+1)]: # 경사로가 겹치는 경우
                            return("NO")
                            break
    if i==N-2: return("YES")
    else : return("NO")

count_row = 0
for row in range(N):
#    print(is_path(X[row], N, L))
    if is_path(X[row], N, L)=="YES": 
        count_row += 1

count_col = 0
for col in range(N):
#    print(is_path([i[col] for i in X], N, L))
    if is_path([i[col] for i in X], N, L)=="YES":
        count_col += 1

print(count_row + count_col)

#%%

path = [3,2,2,1,1,1]
is_path(path, N, L)
