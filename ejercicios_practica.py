#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Emmanuel Oscar Torres Molina"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


def ej1():
  print('\nEjercicios de práctica con números:\n')

  '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
  '''

  print("Ingrese un Número Real:")
  nro_real_1 = float(input( ))

  print("\nIngrese Otro Número Real:")
  nro_real_2 = float (input( ))

  diferencia = nro_real_1 - nro_real_2

  if diferencia > 0:
    print("\n\nLa diferencia entre el 1er Número Ingresado y el 2do Número Ingresado es POSITIVO.\n")

  elif diferencia == 0:
    print("\n\nLa diferencia entre el 1er Número Ingresado y el 2do Número Ingresado es 0.\n")

  else:
      print("\n\nLa diferencia entre el 1er Número Ingresado y el 2do Número Ingresado es NEGATIVO.\n")



def ej2():
  print('Ejercicios de práctica con números')

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
  '''


def ej3():
  print('Ejercicios de práctica con números')

  '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
  '''


def ej4():
  print('Ejercicios de práctica con cadenas')

  '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
  '''


def ej5():
  print('Ejercicios de práctica con números')

  '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
  '''

if __name__ == '__main__':
  print("\nEjercicios de práctica:\n")
  ej1()
  #ej2()
  #ej3()
  #ej4()
  #ej5()
