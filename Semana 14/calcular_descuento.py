def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a una compra.

    Args:
        monto_total (float): El monto total de la compra.
        porcentaje_descuento (float): El porcentaje de descuento a aplicar (por defecto es 10).

    Returns:
        float: El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Solicitar el monto de la compra al usuario
monto_compra = float(input("Ingrese el monto de la compra: $"))

# Definir el porcentaje de descuento predeterminado
porcentaje_descuento = 15

# Calcular el descuento
descuento = calcular_descuento(monto_compra, porcentaje_descuento)

# Calcular el monto final a pagar
monto_final = monto_compra - descuento

# Mostrar los resultados
print(f"Monto de la compra: ${monto_compra:.2f}")
print(f"Descuento aplicado ({porcentaje_descuento:.0f}%): ${descuento:.2f}")
print(f"Monto final a pagar: ${monto_final:.2f}")