# Cap 26-27 - Ejercicio: Rectangulo en Python
"""
Se solicita calcular el Area y el perimetro de un rectangulo, para ello debemos crear la siguientes variables
    alto (int)
    ancho (int)
El usuario debe proporcionar los valores de largo y ancho y despues se debe imprimir  en el siguiente formato
    Proporciona el alto:
    Proporciona el ancho:
    Area:<Area>
    Perimetro:<perimetro>

Las formulas para calcular el area y el perimetro de un rectangulo son:
    Area:alto*ancho
    perimetro:(alto + ancho)*2
"""

alto = int(input('Proporciona el alto del rectangulo:'))
ancho = int(input('Proporciona el ancho del rectangulo:'))
print(f'Area: {alto * ancho}')
print(f'Perimetro: {(alto + ancho) * 2}')
print('------Fin del programa------')
