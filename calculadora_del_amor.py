nombre1 = input("Escriba el primer nombre: ")
nombre2 = input("Escriba el segundo nombre: ")

string_nombres = nombre1 + nombre2

string_nombres_minuscula = string_nombres.lower()

t =  string_nombres_minuscula.count("t")
r =  string_nombres_minuscula.count("r")
u =  string_nombres_minuscula.count("u")
e =  string_nombres_minuscula.count("e")
true = t + r + u + e 


l =  string_nombres_minuscula.count("l")
o =  string_nombres_minuscula.count("o")
v =  string_nombres_minuscula.count("v")
e =  string_nombres_minuscula.count("e")
love = l + o + v + e 

puntaje = true + love

print(puntaje)

if (puntaje <=10 ) or (puntaje >= 90):
    print("lo siento, no puden estar juntos")
elif(puntaje >=40) and (puntaje <= 50):
    print("felicidades, pueden estar juntos")
 
else:
    print(f"Puntaje: {puntaje}")

