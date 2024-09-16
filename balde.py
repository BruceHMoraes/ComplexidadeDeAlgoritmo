def balde(x):
    qtdBaldes = len(x)
    baldes = [[] for _ in range(qtdBaldes)] # é uma lista para cada elemento dentro de uma lista 

    for num in x:
        index = num - 1
        baldes[index].append(num)

    x =[]
    for balde in baldes:
        x.extend(balde)
    return x # extende cada elemento para sua respectiva ordem.

print(balde([2,4,1,1,3,2,7,4,6]))    


# Tempo O(n)
# Espaço O(n)  
# 
#
