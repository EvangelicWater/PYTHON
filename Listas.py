#leer 5 numeros e imprimirlos del mas pequeño al mas grande

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers.sort()
print("Lista ordenada:",numbers);



numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

del numbers[0]
print("Contenido de lista con valor eliminado:",numbers)
print("Nueva longitud de la lista:",len(numbers))

#Un elemento con un índice igual a -1 es el último en la lista
print("Ultimo elemento de la lista:",numbers[-1])

#Del mismo modo, el elemento con un índice igual a -2 es el anterior al último en la lista.
print("Numero anterior al ultimo de la lista:",numbers[-2])

#reemplazar un elemento de la lista con un numero deseado
numbers[0] = int(input("Ingresa un número entero: "))
print("Nueva Lista con tu numero ingresado:",numbers)

#agregar un numero al final de la lista existente

numbers.append(7)
print("Nueva Lista modificada con append:",numbers,"con longitud:",len(numbers))
numbers.insert(4, 22)
print("Nueva Lista modificada con insert:",numbers,"con longitud:",len(numbers))

numbers.reverse()
print("Lista invertida:",numbers)

#copiar una lista a otra

copia=numbers[:]
print("Copia:",copia,"Con longitud:",len(copia))

copy=numbers[0:5]

print("Copia de la lista original empezando por la posicion 0 hasta la posicion 5",copy,"Con longitud:",len(copy))
#se podria utilizar copy=numbers[0:-1] y copiaria la lista excepto el ultimo elemento porque -1 significa final, final de la lista

del copy[1:3]#elimina desde la primera posicion y se detiene en la tercera posicion
print("Copia con secciones eliminadas:",copy,"Con longitud:",len(copy))

#de igual manera del copy[:]eliminaria todos los elementos de la lista

