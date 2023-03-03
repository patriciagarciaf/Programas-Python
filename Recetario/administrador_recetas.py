import sys
from pathlib import Path
from os import system
import os

base = Path.home()
base_recetas = Path(base, 'Recetas')


def ir_a_menu_principal():
    print('[1] - Leer receta \n[2] - Crear receta\n[3] - Crear categoria\n'
          '[4] - Eliminar receta\n[5] - Eliminar categoria\n[6] - Finalizar programa ')
    eleccion = input('Elige una opción: ')
    system('cls')

    while eleccion != '6':
        if eleccion == '1':
            ruta_categoria = elegir_categoria()
            ruta_receta = elegir_receta(ruta_categoria)
            leer_receta(ruta_receta)
            volver_salir()
            system('cls')
            break

        elif eleccion == '2':
            ruta_categoria = elegir_categoria()
            crear_receta(ruta_categoria)
            volver_salir()
            system('cls')
            break

        elif eleccion == '3':
            crear_categoria()
            volver_salir()
            system('cls')
            break

        elif eleccion == '4':
            ruta_categoria = elegir_categoria()
            eliminar_receta(ruta_categoria)
            volver_salir()
            system('cls')
            break

        elif eleccion == '5':
            eliminar_categoria()
            volver_salir()
            system('cls')
            break

        else:
            ir_a_menu_principal()
    print('Salió del programa')
    sys.exit()


def elegir_categoria():
    i = 1
    for txt in base_recetas.glob('*'):
        print(f'[{i}] - ', txt.stem)
        i += 1
    categoria = input('Elige una categoria: ')
    ruta_categoria = list(base_recetas.glob('*'))[int(categoria) - 1]
    system('cls')
    return ruta_categoria


def elegir_receta(ruta_categoria):
    i = 1
    for txt in list(ruta_categoria.glob('*.txt')):
        print(f'[{i}] - ', txt.stem)
        i += 1
    receta = input('Elegir receta: ')
    ruta_receta = list(ruta_categoria.glob('*.txt'))[int(receta) - 1]
    system('cls')
    return ruta_receta


def leer_receta(ruta_receta):
    print(ruta_receta.read_text())


def crear_categoria():
    categoria = input('Introduce el nombre de la nueva categoría: ')
    os.makedirs(Path(base_recetas, categoria))
    system('cls')
    print(f'Carpeta {categoria} creada con éxito')


def eliminar_categoria():
    i = 1
    for txt in base_recetas.glob('*'):
        print(f'[{i}] - ', txt.stem)
        i += 1
    categoria_eliminar = input('Elige una categoria para eliminar: ')
    ruta_categoria_eliminar = list(base_recetas.glob('*'))[int(categoria_eliminar) - 1]
    os.rmdir(ruta_categoria_eliminar)
    system('cls')
    print('La categoria ha sido eliminada con éxito')


def crear_receta(ruta_categoria):
    os.chdir(ruta_categoria)
    nombre_receta = input('Introduce el nombre de la receta: ')
    archivo = open(nombre_receta + '.txt', 'w')
    receta_texto = input('Introduce la receta: ')
    archivo.write(receta_texto)
    archivo.close()
    system('cls')
    print(f'Receta {nombre_receta} creada con éxito')
    os.chdir(base_recetas)


def eliminar_receta(ruta_categoria):
    i = 1
    for txt in list(ruta_categoria.glob('*.txt')):
        print(f'[{i}] - ', txt.stem)
        i += 1
    receta_eliminar = input('Elegir receta a eliminar: ')
    ruta_receta_eliminar = list(ruta_categoria.glob('*.txt'))[int(receta_eliminar) - 1]
    os.remove(ruta_receta_eliminar)
    system('cls')
    print('Receta eliminada con éxito')


def volver_salir():
    variable = input('\n¿Quieres volver al menú (v) o salir (s)?')
    while variable != 's':
        if variable == 'v':
            system('cls')
            ir_a_menu_principal()
        else:
            system('cls')
            print('Pulsa una tecla correcta')
            variable = input('\n¿Quieres volver al menú (v) o salir (s)?')


ir_a_menu_principal()
