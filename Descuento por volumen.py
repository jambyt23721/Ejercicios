cantidad = int(input("Ingrese la cantidad de camisas: "))

if cantidad <= 0:
    print("Error: La cantidad debe ser mayor a cero.")
else:
    precio_unitario = 15.0
    subtotal = cantidad * precio_unitario

    if cantidad <= 10:
        descuento = subtotal * 0.0
    elif cantidad <= 50:
        descuento = subtotal * 0.10
    elif cantidad <= 100:
        descuento = subtotal * 0.15
    else:
        descuento = 0.20

    total_con_descuento = subtotal - descuento
    print(f"Subtotal: {subtotal}")
    print(f"Descuento aplicado: {descuento}")
    print(f"Total a pagar: {total_con_descuento}")