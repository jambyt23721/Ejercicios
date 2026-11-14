a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("El Triangulo es valido.")
else:
    print("El Triangulo no es valido.")