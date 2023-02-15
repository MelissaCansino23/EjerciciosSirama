# pedimos al ususario que omgrese un numero
num = int(input("ingrese un numero: "))

if num == 1:
    print("El numero 1, no es primo. ")
elif num > 1:
    #Revisar si encontramos factores
    for i in range(2,num): # for desde el numero 2, hasta num -1 para realizar las operaciones
        if num % i == 0: #Si un numero me da una division exacta desde el 2 hasta el numero -1, ya no es primo 
            print(f"El numero {num}, no es primo.")
            print(i, "*" , num//i, "es", num)
            break #se rompe el bucle en el primer factor que encuentra
    else:
        print(f"El numero {num}, si es primo. ")
else:
    print("el numero {num} es negativo, por lo tanto no es primo")
