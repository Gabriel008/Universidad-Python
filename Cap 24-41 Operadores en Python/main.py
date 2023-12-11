# Cap 36 - Ejercicio: Rango entre 20's y 30's en Python

edad = int(input('Intruduce tu edad: '))

"""veintes = edad >= 20 and edad < 30
print("20's:", veintes)
treintas = edad >= 30 and edad < 40
print("30's:", treintas)"""

if (edad >= 20 and edad < 30) or (edad >= 30 and edad < 40):
    print('Dentro de rango 20\'s o 30\'s')
    """    
        if veintes:
            print("Dentro de los 20's")
        elif treintas:
            print("Dentro de los 30's")
        else:
            print('Fuera de rango')
    """
else:
    print("No esta dentro de los 20's ni 30's")
