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

        quicksort(array, inicio, f)
        quicksort(array, i, fim)

if __name__ == "__main__":
    array = [10, 2, 1, 11, 12]
    quicksort(array, 0, len(array) - 1)
    print(array)