import random
vetor = [None] * 5341
colisao = 0
for i in range(2000):
    valor = random.randrange(1,10**6)
    posicao = valor % 5341
    if vetor[posicao] != None:
        colisao +=1
    vetor[posicao] = valor
print(colisao)