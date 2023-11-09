def quicksort(array, inicio, fim):
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

        print(f"Pivô: {pivot}")
        print(f"Subvetor à esquerda: {array[inicio:f+1]}")
        print(f"Subvetor à direita: {array[i:fim+1]}\n")

        quicksort(array, inicio, f)
        quicksort(array, i, fim)

if __name__ == "__main__":
    array = [65, 77, 51, 25, 3, 84, 48, 21, 5]
    quicksort(array, 0, len(array) - 1)