import random

ciudades = ["Quito", "Riobamba", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

matriz_temperaturas = []

for ciudad in ciudades:
    matriz_ciudad = []
    for semana in semanas:
        matriz_semana = []
        for dia in dias_semana:
            # Generar temperaturas aleatorias entre 10 y 30 grados para simular datos reales
            temperatura = random.randint(10, 30)
            matriz_semana.append(temperatura)
        matriz_ciudad.append(matriz_semana)
    matriz_temperaturas.append(matriz_ciudad)

def calcular_promedio_ciudades(matriz_temperaturas):
    """
    Calcula el promedio de temperatura para cada ciudad.

    Args:
        matriz_temperaturas (list): Matriz con las temperaturas de cada ciudad.

    Returns:
        dict: Diccionario con el promedio de temperatura por ciudad.
    """

    promedios_ciudades = {}
    for i, ciudad in enumerate(ciudades):
        total_temperaturas = 0
        total_dias = 0
        for semana in matriz_temperaturas[i]:
            for temperatura in semana:
                total_temperaturas += temperatura
                total_dias += 1
        promedio = total_temperaturas / total_dias
        promedios_ciudades[ciudad] = promedio
    return promedios_ciudades

promedios_por_ciudad = calcular_promedio_ciudades(matriz_temperaturas)

for ciudad, promedio in promedios_por_ciudad.items():
    print(f"Promedio de temperatura en {ciudad}: {promedio:.2f} grados")