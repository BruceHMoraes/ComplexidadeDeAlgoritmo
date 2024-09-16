def exd (x, y):
    r = 0
    while y > 0:
        if y % 2 == 1:
            r =r + x
        x = x + x
        y = y // 2
    return r

print(exd(5,6))        

# multiplicação entre dois elementos
# tempo O(lg n)
# espaço O(1)