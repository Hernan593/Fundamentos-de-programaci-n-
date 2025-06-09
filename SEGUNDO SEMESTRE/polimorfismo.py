"""
Ejemplo de Polimorfismo: Sistema de procesamiento de pagos
"""


class MetodoPago:
    def procesar_pago(self, monto):
        pass


class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con Tarjeta de Crédito"


class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado con PayPal"


class TransferenciaBancaria(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago de ${monto} procesado por Transferencia Bancaria"


def realizar_pago(metodo, monto):
    print(metodo.procesar_pago(monto))


# Caso de uso
if __name__ == "__main__":
    metodos_pago = [
        TarjetaCredito(),
        PayPal(),
        TransferenciaBancaria()
    ]

    for metodo in metodos_pago:
        realizar_pago(metodo, 150.50)