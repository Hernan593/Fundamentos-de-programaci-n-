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

promedios_semanales = []

for i, ciudad in enumerate(ciudades):
    promedios_ciudad = []
    for j, semana in enumerate(semanas):
        temperaturas_semana = matriz_temperaturas[i][j]
        promedio = sum(temperaturas_semana) / len(temperaturas_semana)
        promedios_ciudad.append(promedio)
    promedios_semanales.append(promedios_ciudad)

for i, ciudad in enumerate(ciudades):
    print(f"Promedios de {ciudad}:")
    for j, semana in enumerate(semanas):
        print(f"  {semana}: {promedios_semanales[i][j]:.2f} grados")