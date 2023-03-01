#AHORCADO DE COLORES
from random import choice


'''
funciones para
- pedir letra
- validar letra
- chequear letra
- ver si ganó
'''

palabras_posibles = ['amarillo', 'azul', 'rojo', 'rosa', 'violeta', 'verde', 'naranja', 'blanco', 'negro', 'marron']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def randomizar_palabra():
    palabra_secreta = choice(palabras_posibles)
    letras_unicas = len(set(palabra_secreta))
    return palabra_secreta, letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra válida')
    return letra_elegida


def mostrar_nuevo_tablero(palabra_secreta):
    lista_oculta = []
    for letra in palabra_secreta:
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')
    print(' '.join(lista_oculta))


def chequear_letra(letra_elegida, palabra_secreta, vidas, coincidendias):
    fin = False
    if letra_elegida in palabra_secreta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidendias += 1
    elif letra_elegida in palabra_secreta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra. Intenta con otra diferente')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidendias == letras_unicas:
        fin = ganar(palabra_secreta)

    return vidas, fin, coincidendias

def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra secreta era: {palabra}')
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones, has adivinado la palabra!')
    return True

palabra, letras_unicas = randomizar_palabra()
while not juego_terminado:
    print('\n' + '*' *20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' *20 + '\n')
    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)

    juego_terminado = terminado