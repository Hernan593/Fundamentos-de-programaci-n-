"""
Ejemplo de Abstracción: Definimos una interfaz para dispositivos de almacenamiento
"""
from abc import ABC, abstractmethod


class DispositivoAlmacenamiento(ABC):
    @abstractmethod
    def leer_datos(self):
        pass

    @abstractmethod
    def escribir_datos(self, datos):
        pass


class DiscoDuro(DispositivoAlmacenamiento):
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.datos = []

    def leer_datos(self):
        return " ".join(self.datos)

    def escribir_datos(self, datos):
        if len(self.datos) < self.capacidad:
            self.datos.append(datos)
            return True
        return False


# Caso de uso
if __name__ == "__main__":
    mi_disco = DiscoDuro(5)
    mi_disco.escribir_datos("Archivo1")
    mi_disco.escribir_datos("Documento")
    print(f"Datos en disco: {mi_disco.leer_datos()}")