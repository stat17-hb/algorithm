#%%
n = 2
number = 32
from collections import deque
deq = deque([number])
res = deque()

while True:
    temp = deq.popleft()
    deq.append(temp // n) # 몫
    res.appendleft(temp % n) # 나머지
    if temp // n == 0 : break
res


#%%
n = 2
number = 32
res = []

while True:
    q = number // n # 몫
    res[:0] = [number % n] # 나머지
    if number // n == 0 : break # 몫이 0일 때 멈춤
    number = q
res

#%%
n = 26
number = 26
res = ""

while True:
    q = number // n # 몫
    res = str(number % n) + res # 나머지
    if number // n == 0 : break # 몫이 0일 때 멈춤
    number = q
int(res)

#%%

n = 5
number = 10**5
res = ""

while True:
    q = number // n # 몫
    res = str(number % n) + res # 나머지
    if number // n == 0 : break # 몫이 0일 때 멈춤
    number = q
int(res)