def ordenar_fila_matriz(matriz, fila_a_ordenar):
    """
    Ordena una fila específica de una matriz en orden ascendente.

    Args:
        matriz (list): La matriz bidimensional.
        fila_a_ordenar (int): El índice de la fila que se va a ordenar.

    Returns:
        list: La matriz con la fila ordenada.
    """

    fila = matriz[fila_a_ordenar].copy()  # Crear una copia de la fila para no modificar la original
    fila.sort()  # Ordenar la copia de la fila
    matriz[fila_a_ordenar] = fila # Reemplazar la fila original con la ordenada

    return matriz

# Crear una matriz de ejemplo (3x3)
matriz_original = [
    [9, 2, 5],
    [1, 8, 3],
    [6, 4, 7]
]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz_original:
    print(fila)

# Ordenar la primera fila (índice 0)
fila_a_ordenar = 0
matriz_ordenada = ordenar_fila_matriz(matriz_original, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz_ordenada:
    print(fila)