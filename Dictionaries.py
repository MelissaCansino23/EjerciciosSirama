dict = {
    "Bug" : "Un error en el programa.",
    "Funcion": "Una parte del codigo",
}

#Mandando a llamar un valor
print(dict["Funcion"])

#guardando nuevos elementos
dict["loop"] = "Algo repetitivo"

print(dict["loop"])

#creando diccionarios vacios
dict_vacio = {}

#Editando elementos de un diccionario
dict["Bug"] = "una mosca pegada en la pared"
print(dict)
