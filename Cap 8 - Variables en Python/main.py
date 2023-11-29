# Cap 10 - Direccion de memoria y Variables en Python
x = 10 #Cada uno de estos valores es un literal. Es decir, literal 10 asignado a la variable x
y = 2 #Pero como se a comentado estas literales se almacenan en una posicion de memoria y la variable apunta a esa direccion de memoria
z = x + y
print(x)
print(y)
print(z)

#Para saber la direccion de memoria a la que apunta la variable se utiliza la funcion id de la siguiente manera:
print(id(x)) #posicion de memoria donde se encuentra el valor que almacena la variable x en este caso la literal 10
print(id(y))
print(id(z))