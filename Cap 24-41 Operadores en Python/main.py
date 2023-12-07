# Cap 31 - Ejercicio: Determinar si es mayor de edad
"""
                    Algoritmo MayorEdad
                                |
                                v
                       'Escribe tu edad: '
                                |
                                v
                              edad
                                |
                                v
                        <- edad >= 18 ->
F:'Eres menor de edad'                    T:'Eres mayor de edadr'
"""

edad = int(input('Escribe tu edad: '))
if (edad >= 18):
    print(f'Tu edad es: {edad}. Eres mayor de edad')
else:
    print(f'Tu edad es: {edad}. Eres menor de edad')

print('--- Fin algoritmo ---')
