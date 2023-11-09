def recursao(i):
    if i < 0:
        return
    print(i)
    recursao(i-1)

def fat(i):
    if i < 2:
        return i
    return i * fat(i-1)

def soma_ate_n(N):
    x = N
    if x == N:
        return x
    return 


print(fat(30))