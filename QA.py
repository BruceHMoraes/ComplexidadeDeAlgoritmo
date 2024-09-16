x=[5,3,4,65,7,8,9]
def qa(x):
    n = len(x)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if x[i]>x[j]:
                x[i],x[j] = x[j],x[i]
                print(x)
    return x            
print(qa(x))
