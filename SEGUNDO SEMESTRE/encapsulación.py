"""
Ejemplo de Encapsulación: Sistema de control de acceso a una cuenta
"""


class CuentaSegura:
    def __init__(self, usuario, contraseña):
        self.__usuario = usuario
        self.__contraseña = contraseña
        self.__saldo = 0

    def autenticar(self, usuario, contraseña):
        return self.__usuario == usuario and self.__contraseña == contraseña

    def depositar(self, cantidad, usuario, contraseña):
        if self.autenticar(usuario, contraseña) and cantidad > 0:
            self.__saldo += cantidad
            return True
        return False

    def obtener_saldo(self, usuario, contraseña):
        if self.autenticar(usuario, contraseña):
            return self.__saldo
        return "Acceso denegado"


# Caso de uso
if __name__ == "__main__":
    cuenta = CuentaSegura("admin", "1234")
    cuenta.depositar(1000, "admin", "1234")
    print(f"Saldo actual: {cuenta.obtener_saldo('admin', '1234')}")