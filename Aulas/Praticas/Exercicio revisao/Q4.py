from collections import deque
pilha = deque()
descartadas = []
n = 6

for i in range(n,0,-1):
    pilha.append(i)
    if len(pilha) >=2:
        descartadas = pilha.pop()

print(f"Cartas descartadas: ")
for i in descartadas:
    print(i,end = " ")
print(f"Carta remanescente: {pilha[0]}")