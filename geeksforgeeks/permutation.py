#%%
def permutation(lst):
    if len(lst)==1: return([lst]) # list끼리 concatenate 하려면 원소가 하나인 경우를 다시 리스트 안에 넣어줘야 함
    res = []
    for i in range(len(lst)): # 리스트의 모든 i에 대해 반복
        fix = [lst[i]] # int
        remain = lst[:i] + lst[i+1:] # i번째 원소를 제외한 나머지 원소들로 다시 리스트를 만들어줌
        for j in permutation(remain): # 나머지 원소들의 permuation을 고정시킬 원소 뒤에 붙여주면 됨
            res.append(fix + j) # fix가 int라서 list안에 넣어줘야 함
    return(res)

permutation([1,2,3])

for i in permutation([1,2,3,4]): print(i)

permutation([1])
