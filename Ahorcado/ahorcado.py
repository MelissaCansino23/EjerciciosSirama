import random
import ahorcado_art
import ahorcado_palabras 

print(ahorcado_art.logo)
palabra_random = random.choice(ahorcado_palabras.word_list)
size_palabra = len(palabra_random)

display = []
game_over = False
vidas = 6 

for l in range(size_palabra):
    display += "_"

while not game_over:
    letra_usuario = input("adivina una letra: "). lower()

    for posisicon in range(size_palabra):
        letra = palabra_random[posisicon]
        
        if letra == letra_usuario:
            display[posisicon] = letra
    if letra_usuario not in palabra_random:
          vidas -=1

    if vidas <=0:
        print("LO SIENTO, PERDISTE!! LA PALABRA ERA: ", palabra_random)
        game_over = True

    if "_" not in display:
         print("FELICIDADES, HAS GANADO!!!!!!")
         game_over = True

    print(' '.join(display))
    print(ahorcado_art.stages[vidas])

    




    