#%%
def to_binary(x):
    res = [0 for i in range(32)]
    binary = []
    while True:
        binary.append(x % 2)
        x = x // 2
        if x // 2 == 0: 
            binary.append(x)
            break
    for j in range(len(binary)):
        res[j] = binary[j]
    return(res[::-1])

bit = []
for i in range(len(to_binary(1))):
    if to_binary(1)[i] == to_binary(2)[i]: bit.append(0)
    else : bit.append(1)

decimal = 0
reverse_bit = bit[::-1]
for j in range(len(bit)):
    if reverse_bit[j]==1: decimal += 2**j
print(decimal)

a = [1,2,3,4]


for i in range(len(a)):
    if i==0: b=a[i]
    else: b ^=a[i] 
b
1^2^3^4


