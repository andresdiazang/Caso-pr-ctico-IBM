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

