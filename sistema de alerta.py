movimiento = input("Hay movimiento? (si/no):? ")
momento = input("Es de día? (si/no):? ")

if movimiento == "si" and momento == "si":
    print("Encender la Alarma movimiento de noche detectado")
elif movimiento == "si" and momento == "no":
    print("movimiento registrado(es de dia, alarma desactivada)")
elif movimiento == "no" and momento == "si":
    print("No hay movimiento, alarma en vigilancia")
else:
    print("No hay movimiento (es de dia). Alarma en reposo)")