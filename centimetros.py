cm = float(input("Ingrese la cantidad de centimetros: "))
if cm < 0:
    print("Error: La cantidad de centimetros no puede ser negativa.")
else:
   pulgadas_totales = cm / 2.54
   pies = pulgadas_totales // 12
   pulgadas = pulgadas_totales % 12
   print(f"{cm} centimetros son equivalentes a: {int(pies)} pies y {int(pulgadas)} pulgadas.")