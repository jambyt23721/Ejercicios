numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    resultado = numero // 2
    print(f"Es par, la mitad es: {resultado}")
else:
    resultado = numero * 2
    print(f"Es impar, el doble es: {resultado}")