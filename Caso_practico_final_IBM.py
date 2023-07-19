import random

#Generando la matriz cuadrada NxN y rellenando con números aleatorios.

def generar_matriz(N):
    matriz = []
    for _ in range(N):
        fila = []
        for _ in range(N):
            fila.append(random.randint(0,9))
        matriz.append(fila)
    return matriz
    
#Imprimiendo la matriz en la pantalla.

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


#Calculando la suma de los elementos de cada fila y columna, para luego almacenarlos
def calcular_sumas(matriz):
    suma_columnas=[]
    suma_filas=[]
    for fila in matriz:
        suma_filas.append(sum(fila))
    for i in range(len(matriz)):
        suma_columna=sum(fila[i] for fila in matriz)
        suma_columnas.append(suma_columna)
        
    return suma_filas, suma_columnas

# Para imprimir la suma de filas y columnas
def imprimir_sumas(suma_filas, suma_columnas):
    print("Suma de cada fila: ")
    for suma_fila in suma_filas:
        print(suma_fila)
    print("Suma de cada columna:")
    for suma_columna in suma_columnas:
        print(suma_columna)

try:
    N = int(input("Ingrese el tamaño de la matriz cuadrada: "))
    matriz = generar_matriz(N)
    print("Matriz generada:")
    imprimir_matriz(matriz)
    suma_filas, suma_columnas = calcular_sumas(matriz)
    imprimir_sumas(suma_filas, suma_columnas)
except ValueError:
    print("Error: Por favor, ingrese un valor válido para N.")

# Pruebas unitarias básicas
# Matriz 2x2 con elementos predefinidos para verificar la suma de filas y columnas.
matriz_prueba = [[1, 2], [3, 4]]
suma_filas_prueba, suma_columnas_prueba = calcular_sumas(matriz_prueba)
assert suma_filas_prueba == [3, 7]
assert suma_columnas_prueba == [4, 6]