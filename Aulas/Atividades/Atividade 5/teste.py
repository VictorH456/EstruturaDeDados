def selectionSort(vetor, tamanho):
    for i in range(tamanho-2):
        index_menor = i #recebe a posição do menor atual(no primeiro loop recebea primeira)

        for j in range(i+1, tamanho):
            #se o vetor[j] for menor que o valor da posição atual, index_menor recebe j
            if(vetor[j] < vetor[index_menor]): 
                index_menor = j
        
        vetor[i], vetor[index_menor] = vetor[index_menor], vetor[i] #troca o valor de ambas.
        print(vetor)

if __name__ == "__main__":
    n = int(input("Digite um valor inteiro: "))
    vetor = []
    for i in range(n):
        vetor.append(int(input("Digite um valor inteiro: ")))
    print()
    selectionSort(vetor, n)