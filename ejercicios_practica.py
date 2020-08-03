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
  print('\nEjercicios de práctica con números:\n')

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
  '''

  print('\nIngrese un Número Entero:')
  nro_1 = int(input( ))

  print('\nIngrese un 2do Número Entero:')
  nro_2 = int(input( ))

  print('\nIngrese un 3er Número Entero:')
  nro_3 = int(input( ))

  if (nro_1 % 2) == 0:
    print('\n\nEl 1er Número Ingresado es Par.')
  else:
    print('\n\nEl 1er Número Ingresado es Impar.')


  if (nro_2 % 2) == 0:
    print('\nEl 2do Número Ingresado es Par.')
  else:
    print('\nEl 2do Número Ingresado es Impar.')

  
  if (nro_3 % 2) == 0:
    print('\nEl 3er Número Ingresado es Par.\n\n')
  else:
    print('\nEl 3er Número Ingresado es Impar.\n\n')
  



def ej3():
  print('Ejercicios de práctica con números:\n\n')

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

  print("Ingrese un Número Real:")
  numero_1 = float(input( ))

  print("\nIngrese Otro Número Real:")
  numero_2 = float (input( ))

  print('\n\nAhora Ingrese el Símbolo de la Operación que Desee Calcular:\n')
  print('Suma (+)')
  print('Resta (-)')
  print('Multiplicación (*)')
  print('División (/)')
  print('Exponente/Potencia (**)\n')
  print('Ingrese el Símbolo: ')
  simbolo = str(input( ))

  if simbolo == '+':
    result = numero_1 + numero_2
    print('\n\nEl Símbolo Ingresado es:"{}" y el Resultado de la Operación es: {}.'.format(simbolo, result))

  elif simbolo == '-':
    result = numero_1 - numero_2
    print('\n\nEl Símbolo Ingresado es:"{}" y el Resultado de la Operación es: {}.\n\n'.format(simbolo, result))

  elif simbolo == '*':
    result = numero_1 * numero_2
    print('\n\nEl Símbolo Ingresado es: "{}" y el Resultado de la Operación es: {}.\n\n'.format(simbolo, result))

  elif simbolo == '/':
    result = numero_1 / numero_2
    print('\n\nEl Símbolo Ingresado es: "{}" y el Resultado de la Operación es: {}.\n\n'.format(simbolo, result))

  elif simbolo == '**':
    result = numero_1 ** numero_2
    print('\n\nEl Símbolo Ingresado es: "{}" y el Resultado de la Operación es: {}.\n\n'.format(simbolo, result))

  else:
    print('\n\nEl Símbolo Ingresado: "{}" es un Símbolo Matemático Incorrecto.\n\n'.format(simbolo))



def ej4():
  print('Ejercicios de práctica con cadenas:\n\n')

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

  print('Ingrese una 1er Palabra:')
  palabra_1 = str(input( ))
  
  print('\nIngrese una 2da Palabra:')
  palabra_2 = str(input ( ))

  print('\nIngrese una 3ra Palabra:')
  palabra_3 = str(input( ))

  print('\n\nAhora Ingrese El Número Según como quiera Ordenar las Palabras:\n')
  print('1 - Ordenar por Orden Alfabético.')
  print('2 - Ordenar por Cantidad de Letras.')

  print('\nIngrese el Número Correspondiente:')
  opcion = int(input( ))

  if opcion == 1:
    print("\n\nLas Palabras Ingresadas Ordenadas de Mayor a Menor:\n")

    if ((palabra_1 >= palabra_2) and (palabra_2 >= palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_1, palabra_2, palabra_3))

    elif ((palabra_1 >= palabra_2) and (palabra_2 < palabra_3) and (palabra_1 >= palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_1, palabra_3, palabra_2))

    elif ((palabra_1 < palabra_2) and (palabra_1 >= palabra_3) and (palabra_2 >= palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_2, palabra_1, palabra_3))
    
    elif ((palabra_1 < palabra_2) and (palabra_1 < palabra_3) and (palabra_2 >= palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_2, palabra_3, palabra_1))

    elif ((palabra_1 < palabra_2) and (palabra_1 < palabra_3) and (palabra_2 < palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_3, palabra_2, palabra_1))

    elif ((palabra_1 >= palabra_2) and (palabra_1 < palabra_3) and (palabra_2 < palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_3, palabra_1, palabra_2))

    else:
      print("'{}' '{}' '{}'".format(palabra_1, palabra_2, palabra_3))

    print('\n\n')


  elif opcion == 2:
    print("\n\nLas Palabras Ingresadas Ordenadas de Mayor a Menor:\n")

    len_palabra_1 = len(palabra_1)
    len_palabra_2 = len(palabra_2)
    len_palabra_3 = len(palabra_3)

    if ((len_palabra_1 >= len_palabra_2) and (len_palabra_2 >= len_palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_1, palabra_2, palabra_3))

    elif ((len_palabra_1 >= len_palabra_2) and (len_palabra_2 < len_palabra_3)
    and (len_palabra_1 >= len_palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_1, palabra_3, palabra_2))

    elif ((len_palabra_1 < len_palabra_2) and (len_palabra_1 >= len_palabra_3) 
    and (len_palabra_2 >= len_palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_2, palabra_1, palabra_3))
    
    elif ((len_palabra_1 < len_palabra_2) and (len_palabra_1 < len_palabra_3) 
    and (len_palabra_2 >= len_palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_2, palabra_3, palabra_1))

    elif ((len_palabra_1 < len_palabra_2) and (len_palabra_1 < len_palabra_3) 
    and (len_palabra_2 < len_palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_3, palabra_2, palabra_1))

    elif ((len_palabra_1 >= len_palabra_2) and (len_palabra_1 < len_palabra_3) 
    and (len_palabra_2 < len_palabra_3)):
      print("'{}' '{}' '{}'".format(palabra_3, palabra_1, palabra_2))

    else:
      print("'{}' '{}' '{}'".format(palabra_1, palabra_2, palabra_3))

    print('\n\n')


  else:
    print('\n\nLa Opción Ingresada No es Válida.\n\n')




def ej5():
  print('\nEjercicios de práctica con Números:\n\n')

  '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
  '''

  print('Ingresar 3 Valores de Temperaturas [°C]:\n\n')
  
  print('Ingrese el 1er Valor de Temperatura:')
  temp_1 = float(input( ))

  print('\nIngresar el 2do Valor de Temperatura:')
  temp_2 = float(input( ))

  print('\nIngresar el 3er Valor de Temperatura:')
  temp_3 = float(input( ))


  if ((temp_1 >= temp_2) and (temp_1 >= temp_3)):
    print('\n\n1 - La Máxima Temperatura es: {} °C'.format(temp_1))

  elif ((temp_2 >= temp_1) and (temp_2 >= temp_3)):
    print('\n\n1 - La Máxima Temperatura es: {} °C'.format(temp_2))

  elif ((temp_3 >= temp_1) and (temp_3 >= temp_2)):
    print('\n\n1 - La Máxima Temperatura es: {} °C'.format(temp_3))

  elif ((temp_1 == temp_2) and (temp_2 == temp_3)):
      print('\n\n1 - La Máxima Temperatura es: {} °C'.format(temp_1))



  if ((temp_1 <= temp_2) and (temp_1 <= temp_3)):
    print('\n2 - La Mínima Temperatura es: {} °C'.format(temp_1))

  elif ((temp_2 <= temp_1) and (temp_2 <= temp_3)):
    print('\n2 - La Mínima Temperatura es: {} °C'.format(temp_2))

  elif ((temp_3 <= temp_1) and (temp_3 <= temp_2)):
    print('\n2 - La Mínima Temperatura es: {} °C'.format(temp_3))

  elif ((temp_1 == temp_2) and (temp_2 == temp_3)):
      print('\n2 - La Mínima Temperatura coincide con la Máxima Temperatura y es: {} °C'.format(temp_1))


  promedio_temp = (temp_1 + temp_2 + temp_3) / 3
  print('\n3 - El Promedio de Temperatura es: {:.2f} °C\n\n\n'.format(promedio_temp))

 

if __name__ == '__main__':
  print("\nEjercicios de práctica:\n")
  ej1()
  ej2()
  ej3()
  ej4()
  ej5()
