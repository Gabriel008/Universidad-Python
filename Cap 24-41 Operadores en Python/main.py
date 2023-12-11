# Cap 33 - Ejercicio: valor dentro del rango (AND) en Python

valor = int(input('Escrive el valor: '))
valorMinimo = 0
valormaximo = 5

dentroRango = (valor >= valorMinimo) and (valor <= valormaximo)

if dentroRango:
    print(f'El valor {valor} está dentro de rango')
else:
    print(f'El valor {valor} está fuera de rango')
