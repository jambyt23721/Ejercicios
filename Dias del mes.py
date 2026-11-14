mes = int(input("Ingrese el número del mes (1-12): "))
dias = 0

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    dias = 31

elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    dias = 30

elif mes == 2:
    dias = 28
    
else:
    print("el mes tiene 31 dias")

print(f"El mes {mes} tiene {dias} días.")