print("Bienvenidos a la montaña Rusa!!")

estatura = int(input("Cual es tu estatura en cm?"))

if estatura > 120:

    print("FELICIDADES PUEDES SUBIR")
    edad = int(input("Ingresa la edad: "))
    if edad < 7:
        print("Muy pequeño, no te puedes subir")
    if edad < 12:
       print("pagas 5 $$")
    elif edad <= 18:
        print("pagas 7$$")
    elif edad >= 80:
        print("por su seguridad le recomendamos no subir")
    else:
        print("pagas 12$$")
        print("DISFRUTA TU VIAJE") 

 