# Cap 40-41 - Ejercicio: Tienda de libros en Python

"""
    Instrucciones:
    Proporciones los siguientes datos del libro:
    Proporciona el nombre:
    Proporciona el ID (numero):
    Proporciona el precio(flotante):
    Indicar si el envio es gratuito (True/False):

    Imprimir=
    Nombre: <>
    Id: <>
    Precio: <>
    Envio Gratuito: <>
"""

print('|--------------------------------------------|')
print(' Proporciones los siguientes datos del libro: ')
print('|--------------------------------------------|')
nombre = input('Proporciona el nombre: ')
id = int(input('Proporciona el ID: '))
precio = float(input('Proporciona el precio: '))
envioGratuito = input('Indicar si el envio es gratuito (True/False): ')

if envioGratuito == 'True':
    envioGratuito = True
elif envioGratuito == 'False':
    envioGratuito = False
else:
    envioGratuito = 'Valor incorrecto, debe escribir True/False'

print(f"""
|----------------------------------------------------|
    Nombre:             {nombre}
    Id:                 {id}
    Precio:             {precio}
    Envio Gratuito?:    {envioGratuito}
|----------------------------------------------------|
""")
