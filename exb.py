def exb(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = [0,1]
        while len(f) < n+1:
            nf = f[-1] + f[-2] #fibonacci
            f.append(nf)
        return f[len(f)-1]
        
        
exb(6)    

# sequência de fibonacci
# tempo = O(n)
# espaço = O(n)
#