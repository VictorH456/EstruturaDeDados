def Merge(lista, inicio, meio, fim):
    n1 = meio - inicio + 1
    n2 = fim - meio
    B = [None]* n1
    C = [None]* n2

    for i in range(n1):
        B[i] = lista[inicio+i]

    for j in range(n2):
        C[j] = lista[meio + j + 1]
    
    i = 0
    j = 0
    k = inicio

    while i < n1 and j < n2:
        if B[i] <= C[j]:
            lista[k] = B[i]
            i += 1
        else:
            lista[k] = C[j]
            j += 1
        k += 1
    
    while i < n1:
        lista[k] = B[i]
        i += 1
        k += 1
    
    while i < n1:
        lista[k] = C[j]
        i += 1
        k += 1
    


def MergeSort(lista, inicio, fim ):
    if inicio < fim:
        meio = (fim + inicio) // 2
        MergeSort(lista, inicio, meio)
        MergeSort(lista, meio+1, fim)
        Merge(lista, inicio, meio, fim)
        

if __name__ == "__main__":
    arr = [38, 69, 7, 13, 22, 10,38, 69, 7, 13, 22, 10]
    fim = len(arr)-1

    print("Array entrada: ", arr)
    MergeSort(arr, 0, fim)
    print("Array ordenado: ", arr)
