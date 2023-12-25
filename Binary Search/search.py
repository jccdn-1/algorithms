def binary_search(array, item):
    inicio = 0
    fim = len(array)-1

    while inicio <= fim:
        m = (inicio + fim)//2
        if array[m] == item:
            return m
        if m < item:
            inicio = m + 1
        else:
            fim = m - 1
    return None

lista = [1, 2, 3, 4, 70]

print ("indice:" (binary_search(lista, 2)))