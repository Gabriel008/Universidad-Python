# Cap 38-39 - Ejercicio: el mayor de dos numeros en Python

"""
    Instrucciones:
    Solicitar al usuario dos valores y determinar cual numero es el mayor
    Solicitar al usuario dos valores :
    numero1 (int)
    numero2 (int)
    Se debe imprimir el mayor de los dos numeros (La salida debe ser identica a la que sigue):
    Proporciona ek numero1:
    Proporciona ek numero2:
    El numero mayor es: <numeroMayor>
"""
numero1 = int(input('Proporciona el Numero 1:'))
numero2 = int(input('Proporciona el Numero 2:'))

if numero1 > numero2:
    print(f'Numero 1 mayor es: {numero1}')
else:
    print(f'Numero 2 mayor es: {numero2}')
