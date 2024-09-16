from Numero import Numero

y = [3,5,9,7,6,1,2,4]
x=[]

for i in y:
    x.append(Numero(i))
while len(x)>1:
    k = []
    for i in range(0, len(x),2):
        if i+1 < len(x):
            a,b = x[i],x[i+1]
            if a.maiorQue(b):
                a.ganhouDe(b)
                k.append(a)
            else:
                b.ganhouDe(a)
                k.append(b)
        else:
            k.append(x[i])
    x=k
print(x[0].maiores())                            # n + log n = O(n)
