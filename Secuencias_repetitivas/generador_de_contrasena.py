import random

letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A","B", "C","D", "E","F","G", "H", "I", "J","K","L","M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
simbolos = ["!", "#", "$", "%", "&", "(,)", "*", "+"]

nr_letras = int(input("cuantas letras quieres en tu contraseña?\n"))
nr_simbolos = int(input("cuantos simbolos?\n"))
nr_numeros = int(input("cuantos numeros?\n"))

password = []

for letra in range(nr_letras):
    indice_random_letras = random.randint(0, len(letras)-1)
    password.append(letras[indice_random_letras])

for numero in range(nr_numeros):
    password.append(random.choice(numeros))

password.append(''.join(random.choices(simbolos, k=nr_simbolos)))


print(''.join(password))
random.shuffle(password)
print(''.join(password))





