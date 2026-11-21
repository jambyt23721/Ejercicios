print("--- CAJERO AUTOMÁTICO ---")

monto = int(input("Ingresa el monto a retirar (múltiplo de 10): "))

if monto > 0 and monto % 10 == 0:
    b100 = monto // 100
    resto = monto % 100

    b50 = resto // 50
    resto = resto % 50

    b20 = resto // 20
    resto = resto % 20

    b10 = resto // 10

    print("Billetes entregados:")
    print("De 100:", b100)
    print("De 50:", b50)
    print("De 20:", b20)
    print("De 10:", b10)
else:
    print("Error: El monto debe ser mayor a 0 y múltiplo de 10.")
