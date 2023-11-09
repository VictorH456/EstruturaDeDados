def insertSort_v2(vetor):
    size = len(vetor)

    for i in range(size):
        j = i
        while(j > 0 and vetor[j][1] < vetor[j-1][1]):
            if vetor[j][1] < vetor[j-1][1]:
                vetor[j][1], vetor[j-1][1] = vetor[j-1][1], vetor[j][1]
                vetor[j][0], vetor[j-1][0] = vetor[j-1][0], vetor[j][0]
            j = j - 1

while True:
    lista = []
    try:
        n = int(input())
        for i in range(n):
            carne, num = input().split(" ")
            lista.append([carne, int(num)])
        
        insertSort_v2(lista)
        
        for i in range(len(lista)):
            if(i < len(lista)-1):
                print(f"{lista[i][0]}",end=" ")
            else: 
                print(f"{lista[i][0]}")
    except EOFError:
        break