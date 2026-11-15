a = float(input("ingrese el primer numero:"))
b = float(input("ingrese el segundo numero:"))
c = float(input("ingrese el tercer numero:"))
if a > b and a > c:
    mayor, medio, menor = a, b, c
elif a > c and c > b:
    mayor, medio, menor = a, c, b
elif b > a and a > c:
    mayor, medio, menor = b, a, c
elif b > c and c > a:
    mayor, medio, menor = b, c, a
elif c > a and a > b:
    mayor, medio, menor = c, a, b
elif c > b and b > a:
    mayor, medio, menor = c, b, a
else:
    print("Error: Los números ingresados no son distintos.")
print(f"El mayor es: {mayor}, el medio es: {medio}, y el menor es: {menor}.")