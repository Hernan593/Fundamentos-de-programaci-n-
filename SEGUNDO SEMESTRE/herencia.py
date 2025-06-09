"""
Ejemplo de Herencia: Sistema de empleados con diferentes roles
"""


class Empleado:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def describir_rol(self):
        return "Soy un empleado"


class Gerente(Empleado):
    def describir_rol(self):
        return f"{super().describir_rol()}, específicamente un Gerente"


class Desarrollador(Empleado):
    def __init__(self, nombre, id, lenguaje):
        super().__init__(nombre, id)
        self.lenguaje = lenguaje

    def describir_rol(self):
        return f"{super().describir_rol()}, programo en {self.lenguaje}"


# Caso de uso
if __name__ == "__main__":
    empleados = [
        Empleado("Carlos", 100),
        Gerente("Ana", 101),
        Desarrollador("Luis", 102, "Python")
    ]

    for emp in empleados:
        print(f"{emp.nombre}: {emp.describir_rol()}")