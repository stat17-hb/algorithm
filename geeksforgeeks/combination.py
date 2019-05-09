#%%
n=100
m=6

memo={}
def facto(n):
    if n==0 : memo[n]=1
    else : memo[n] = n*facto(n-1)
    return(memo[n])

print(int(facto(n)/(facto(m)*facto(n-m))))


#%%
n=6
m=2
res=1
for i in range(m):
    res = res*(n-i)/(i+1)
    
print(int(res))

#%%
n=6
m=2
res=1
for i in range(n-m):
    res = res*(m+i+1)/(i+1)
    
print(int(res))


#%%
n=6
m=2
res=1
for i in range(m):
    res = res*(n-m+i+1)/(i+1)
    
print(int(res))

#%%
n=100
m=6
a=1
b=1
for i in range(m):
    a = a*(n-m+i+1)
    b = b*(i+1)
    
print(int(a//b))