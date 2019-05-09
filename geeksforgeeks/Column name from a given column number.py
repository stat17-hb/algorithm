#%%

def colnames(n):
    res = ""
    while n > 0:
        mod = n % 26
        if mod == 0: 
            res = "Z" + res
            n = n//26 - 1
        else:
            mod = n % 26
            res = chr(mod-1 + ord("A")) + res
            n = n//26
    return(res)
    
colnames(26*26)

