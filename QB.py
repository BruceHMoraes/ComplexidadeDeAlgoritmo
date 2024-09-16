x = [2,4,1,90,4,6]    #Bubble sort = O(n²)
def qb (x):          #Espaço = O(n)
    n = len(x)
    for i in range (0, n-1):
        for j in range (n-1,0,-1):
            if x[j-1]>x[j]:
                x[j],x[j-1] = x[j-1], x[j]
    return x           
print (qb(x))
