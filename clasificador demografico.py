edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("Error")
elif edad <= 12:
    print("Es un niño.")
elif edad <= 17:
    print("Es un adolescente.")
elif edad <= 64:
    print("Es un adulto.")
else:
    print("Es un adulto mayor.")