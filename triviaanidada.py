r1 = input("¿Quien Descubrio America?: ")

if r1 == "Cristobal Colon":
    print("Correcto. Pasa a la Siguiente Pregunta!")
    

    r2 = input("¿Cual es la capital de Francia?: ")
    
    if r2 == "Paris":
        print("Correcto. Pasa a la Ultima Pregunta!")
        
     
        r3 = input("¿En que Año Comenzo la Segunda Guerra Mundial?: ")
        
        if r3 == "1939":
            print("Correcto. Has Ganado el Juego de la Muerte!")
        else:
            print("Incorrecto. Has Muerto!")
            
    elif r2 != "Paris":
        print("Incorrecto. Has Muerto!")

elif r1 != "Cristobal Colon":
    print("Incorrecto. Has Muerto!")