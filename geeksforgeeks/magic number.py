#%%

def binary_add(x, i):
    if x[i]==2:
        x[i]=0
        x[i+1]=x[i+1]+1

def binary_magic_num(n):
    x = [0 for i in range(10**2)]
    for j in range(n):
        x[0]=x[0]+1
        for k in range(len(x)-1):
            binary_add(x, k)
    return(x)

a = binary_magic_num(10001)
res = 0
for i in range(len(a)):
    if a[i]==1: res += 5**(i+1)
print(res)


