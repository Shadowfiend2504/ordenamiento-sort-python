import random

def lista1(n):
    lista=[0] * n
    for i in range(n):
        lista[i]=random.randint(0,1000000)
    return lista
print("Ingrese la cantidad de datos que desea para la lista: ")
n=int(input())

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numeros = lista1(n)
print("Lista desordenada:", numeros)

bubble_sort(numeros)
print("Lista ordenada:", numeros)