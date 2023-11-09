def quicksort_nao_recursivo(array, inicio, fim):
    lista = [(inicio, fim)]

    while lista:
        inicio, fim = lista.pop()
        if inicio < fim:
            pivot = array[inicio]
            i = inicio
            f = fim

            while i <= f:
                while array[i] < pivot:
                    i += 1
                while array[f] > pivot:
                    f -= 1
                if i <= f:
                    array[i], array[f] = array[f], array[i]
                    i += 1
                    f -= 1

            if inicio < f:
                lista.append((inicio, f))
            if i < fim:
                lista.append((i, fim))

if __name__ == "__main__":
    array = [65, 77, 51, 25, 3, 84, 48, 21, 5]
    quicksort_nao_recursivo(array, 0, len(array) - 1)
    print("Vetor Ordenado:", array)
