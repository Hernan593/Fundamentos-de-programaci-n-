matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

def buscar_valor(matriz, valor_buscado):
    for fila_index, fila in enumerate(matriz):
        for columna_index, valor in enumerate(fila):
            if valor == valor_buscado:
                return fila_index, columna_index
    return None

valor_buscado = 11
resultado = buscar_valor(matriz, valor_buscado)

if resultado:
    fila, columna = resultado
    print(f"El valor {valor_buscado} se encontró en la posición ({fila}, {columna}).")
else:
    print(f"El valor {valor_buscado} no se encontró en la matriz.")