def ordenar(vetor):
    size = len(vetor)
    for i in range(size):
        j = i
        while(j > 0 and vetor[j] < vetor[j-1]):
            if vetor[j] < vetor[j-1]:
                vetor[j], vetor[j-1] = vetor[j-1], vetor[j]
            j = j - 1
    
    for i in range(size-1):
        j = i
        while(j < size-1):
            if vetor[j] % 2 == 1 and vetor[j+1] > vetor[j]:
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
            j += 1
n = int(input())
vetor = []
for i in range(n):
    num = int(input())
    vetor.append(num)
ordenar(vetor)
for i in vetor:
    print(i)