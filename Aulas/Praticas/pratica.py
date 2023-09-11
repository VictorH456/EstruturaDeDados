def troca( a1, b1):
    global a, b

    y = a
    a = b
    b = y

a = 10
b = 999
troca(a,b)
print(a,b)