#%%

x = 5

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

y = to_binary(x)
decimal = 0
for k in range(len(y)):
    if y[k]==1: decimal += 2**k
    
print(decimal)
