# BubbleSort v1 - ineficiente

def bubbleSort_v1(vetor):
    size = len(vetor)
    interacoes = 0
    for i in range(size):
        interacoes += 1
        for j in range(size-1):
            interacoes += 1
            if(vetor[j] > vetor[j+1]):
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return interacoes 

# BubbleSort v2 - Um pouco melhor

def bubbleSort_v2(vetor):
    size = len(vetor)
    interacoes = 0
    for i in range(size):
        interacoes += 1
        for j in range(size-i-1):
            interacoes += 1
            if(vetor[j] > vetor[j+1]):
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
    return interacoes 

# BubbleSort v3 - Melhor

def bubbleSort_v3(vetor):
    size = len(vetor)
    interacoes = 0
    for i in range(size):
        trocou = False
        interacoes += 1
        for j in range(size-i-1):
            interacoes += 1
            if(vetor[j] > vetor[j+1]):
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]
                trocou = True
        if not trocou:
            break
    return interacoes 


if __name__ == "__main__":

    # vet = [5, 7, -2, 0, 9, 37]
    vet = [2, 5, 7, 6, 9, 10]
    # vet = [1, 2, 4, 6, 8, 9]
    print(vet)
    ite = bubbleSort_v1(vet)
    print("Vetor ordenado buuble v1")
    print(vet)
    print("Interaçoes:", ite)

    vet = [2, 5, 7, 6, 9, 10]
    # vet = [5, 7, -2, 0, 9, 37]
    ite = bubbleSort_v2(vet)
    print("Vetor ordenado buuble v2")
    print(vet)
    print("Interaçoes:", ite)

    vet = [2, 5, 7, 6, 9, 10]
    # vet = [5, 7, -2, 0, 9, 37]
    ite = bubbleSort_v3(vet)
    print("Vetor ordenado buuble v3")
    print(vet)
    print("Interaçoes:", ite)