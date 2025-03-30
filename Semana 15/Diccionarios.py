# 1. Crear un Diccionario
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Riobamba",
    "profesion": "Ingeniero"
}

# 2. Acceder y Modificar Valores
# Modificar la ciudad
informacion_personal["ciudad"] = "Quito"

# Agregar profesión (ya existe, sería actualizar)
# Nota: En las instrucciones dice "agrega", pero la clave ya existe en el paso 1
# Si fuera nueva, sería: informacion_personal["profesion"] = "Nueva profesión"

# 3. Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# 4. Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# 5. Imprimir el Diccionario Final
print("Diccionario final:")
print(informacion_personal)