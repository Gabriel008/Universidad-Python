# Cap 30 - Ejercicio: Numero par o impar
"""
                    Algoritmo par_impar
                                |
                                v
                    'Por favor ingrese un ...'
                                |
                                v
                                a
                                |
                                v
                        <- a mod 2=0 ->
F:'No es un numero par'                    T:'Es un numero par'
"""

a = int(input('Por favor ingrese un numero: '))
if (a % 2 == 0):
    print(f'El valor de a {a} es un numero par')
else:
    print(f'El valor de a {a} es un numero impar')

print('--- Fin algoritmo ---')
