def quicksort_iterativo(array, inicio, fim):
    lista = [(inicio, fim)]

    while lista:
        inicio, fim = lista.pop()
        while inicio < fim:
            pivot = array[inicio]
            i = inicio
            j = fim

            while i < j:
                while array[j] > pivot:
                    j -= 1
                while i < j and array[i] <= pivot:
                    i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]

            array[inicio], array[j] = array[j], array[inicio]
            
            if j - inicio < fim - j:
                lista.append((inicio, j - 1))
                inicio = j + 1
            else:
                lista.append((j + 1, fim))
    
if __name__ == "__main__":
    array = [65, 77, 51, 25, 3, 84, 48, 21, 5]
    inicio, fim = 0, len(array) - 1
    quicksort_iterativo(array, inicio, fim)
    print("Vetor Ordenado:", array)
