# Cap 13 - Tipos de datos en Python
"""
Tipos de datos:

Numeric:(integer, float, Complex Number)
Dictionary
Boolean
Set
Sequense Type:(String, List, Tuple)
"""
x = 10
print(x)
print(type(x), '\n')  # class 'int'

x = "Hola Mundo"
print(x)
print(type(x), '\n')  # class 'str'

x: str = "Hola Mundo2"  # Tambien podemos agregar una pista del tipo de dato (hint = pista o indicacion)
print(x)
print(type(x), '\n')  # class 'str'

x: str = 10  # Esto no define el tipo de la variable (hint = pista o indicacion)
print(x)
print(type(x), '\n')  # class 'int'

x = True  # o False. Respetar mayusculas inicial
print(x)
print(type(x), '\n')  # class 'bool'
