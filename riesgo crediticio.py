print("--- EVALUACIÓN DE CRÉDITO ---")

monto = float(input("Ingresa el monto del préstamo: "))
tasa_anual = float(input("Ingresa el porcentaje de interés anual: "))
anios = int(input("Ingresa el plazo en años: "))
salario = float(input("Ingresa tu salario mensual: "))

tasa_mensual = (tasa_anual / 100) / 12
meses = anios * 12

cuota = (monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** (-meses))
limite_salario = salario * 0.30

print("Cuota mensual estimada:", round(cuota, 2))
print("Límite permitido (30% del salario):", round(limite_salario, 2))

if cuota > limite_salario:
    print("Estado: Crédito DENEGADO")
else:
    print("Estado: Crédito APROBADO")
