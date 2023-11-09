def insertSort(vetor):
    size = len(vetor)
    for i in range(size):
        j = i
        while(j > 0):
            if vetor[j] % 2 == 0 == vetor[j-1] % 2:
                if vetor[j] < vetor[j-1]:
                    vetor[j], vetor[j-1] = vetor[j-1], vetor[j] 

            elif vetor[j] % 2 == 0 and  vetor[j-1] % 2 == 1:
                vetor[j], vetor[j-1] = vetor[j-1], vetor[j]

            elif vetor[j] % 2 == 1 == vetor[j-1] % 2:
                 if vetor[j] > vetor[j-1]:
                    vetor[j], vetor[j-1] = vetor[j-1], vetor[j]     
            j -= 1

n = int(input())
vetor = []
for i in range(n):
    vetor.append(int(input()))

insertSort(vetor)
for i in vetor:
    print(i)

'''
atual é par e anterior é par
    troco se meu atual for menor que meu anterior.
atual é par e anterior é impar
    Troco
atual é impar e anterior é par
    não troco
atual é impar e anterior é impar
    troco se meu atual for maior que meu anterior.
'''