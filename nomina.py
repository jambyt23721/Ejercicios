print("--- CÁLCULO DE NÓMINA ---")

horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa el pago por hora ($): "))

if horas <= 40:
    salario_bruto = horas * tarifa
else:
    horas_extras = horas - 40
    salario_bruto = (40 * tarifa) + (horas_extras * tarifa * 1.5)

if salario_bruto > 1000:
    excedente = salario_bruto - 1000
    impuesto = excedente * 0.10
else:
    impuesto = 0

salario_neto = salario_bruto - impuesto

print("Salario Bruto: $", salario_bruto)
print("Impuesto retenido: $", impuesto)
print("Salario Neto a pagar: $", salario_neto)
