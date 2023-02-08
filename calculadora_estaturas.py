estatura_mama = float(input("Estatura mama: "))
estatura_papa = float(input("Estatura papa: "))

suma_est = estatura_mama + estatura_papa

genero = input("Indique si es niño o niña: ").lower()

if genero == "niño": 
    A = round((suma_est + 0.13) / 2, 2)
elif genero == "niña":
    A = round((suma_est - 0.13) / 2, 2)
else:
    print("Especifique si es niño o niña!") 

print("Altura maxima:", A + 0.07)   
print("Altura minima:",A - 0.07)