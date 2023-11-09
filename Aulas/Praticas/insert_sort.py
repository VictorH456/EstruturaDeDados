def insertSort_v1(vetor):
    size = len(vetor)
    interacoes = 0
    for i in range(size):
        j = i
        interacoes += 1
        while(j>0):
            interacoes += 1
            if vetor[j] < vetor[j-1]:
                vetor[j], vetor[j-1] = vetor[j-1], vetor[j]
            j = j - 1
    return interacoes

def insertSort_v2(vetor):
    size = len(vetor)
    interacoes = 0
    for i in range(size):
        j = i
        interacoes += 1
        while(j > 0 and vetor[j] < vetor[j-1]):
            interacoes += 1
            if vetor[j] < vetor[j-1]:
                vetor[j], vetor[j-1] = vetor[j-1], vetor[j]
            j = j - 1
    return interacoes


if __name__ == "__main__":

    vet = [5, 7, -2, 0, 9, 37]
    print(vet)
    ite = insertSort_v1(vet)
    print("Vetor ordenado Insert v1")
    print(vet)
    print("Interaçoes:", ite)
    
    vet = [5, 7, -2, 0, 9, 37]
    print(vet)
    ite = insertSort_v2(vet)
    print("Vetor ordenado Insert v2")
    print(vet)
    print("Interaçoes:", ite)