# Tarea: Trabajo con Archivos de Texto en Python
# Autor: [Hernan Dario Bonifaz Naranjo]
# Fecha: [6/4/2025]

# 1. Escritura de Archivo de Texto
def escribir_archivo():
    """
    Crea un nuevo archivo llamado my_notes.txt y escribe tres líneas de notas personales.
    """
    try:
        # Abrimos el archivo en modo escritura ('w')
        # Si el archivo no existe, Python lo creará automáticamente
        with open('my_notes.txt', 'w', encoding='utf-8') as archivo:
            # Escribimos tres líneas de notas personales
            archivo.write("Notas personales:\n")
            archivo.write("1. Recordar comprar crocretas para mi mascota mañana.\n")
            archivo.write("2. Llamar al odontologo para pedir cita.\n")
            archivo.write("3. Terminar las tareas antes del Sabado.\n")
        print("Archivo 'my_notes.txt' creado y notas escritas con éxito.")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")


# 2. Lectura de Archivo de Texto
def leer_archivo():
    """
    Función para leer el archivo my_notes.txt línea por línea
    """
    try:
        # Abriendo el archivo en modo lectura ('r')
        with open('my_notes.txt', 'r', encoding='utf-8') as archivo:
            print("\nLeyendo el contenido de 'my_notes.txt':\n")

            # Leemos línea por línea usando un bucle
            linea_numero = 1
            for linea in archivo:
                # Mostramos cada línea con su número
                print(f"Línea {linea_numero}: {linea.strip()}")
                linea_numero += 1
    except FileNotFoundError:
        print("Error: El archivo 'my_notes.txt' no existe.")
    except IOError as e:
        print(f"Error al leer el archivo: {e}")

# Ejecutamos la función
if __name__ == "__main__":
    leer_archivo()