print("--- BOT MÉDICO DE DIAGNÓSTICO ---")
print("Responde exactamente con: si o no")

fiebre = input("¿Tienes fiebre? ")

if fiebre == "si":
    respiracion = input("¿Tienes dificultad para respirar? ")
    if respiracion == "si":
        print("Diagnóstico: Acude a URGENCIAS de inmediato.")
    else:
        print("Diagnóstico: Guarda REPOSO en casa e hidrátate.")
else:
    dolor_cabeza = input("¿Tienes dolor de cabeza? ")
    if dolor_cabeza == "si":
        print("Diagnóstico: Toma una PASTILLA analgésica y descansa.")
    else:
        print("Diagnóstico: Estás SANO.")
