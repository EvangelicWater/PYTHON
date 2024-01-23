dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe' : 5551234567, 'Suzy' : 22657854310}
empty_dictionary = {}

print("Diccionarios originales")
print(dictionary['perro'])
print(phone_numbers['Suzy'])

#los diccionarios no son listas, almacenan pares de valores y cada clave debe ser unica

#no se puede hacer la busqueda de esta manera print(dictionary['chat'])



word=['gato','leon','caballo']
print("Busqueda de palabra en diccionario con for")

for word in word:
    if word in dictionary:
        print(word,"-->",dictionary[word]);

    else:
            print(word,"no esta en el diccionario")
#busca si las palabras estan en el diccionario

print("Recorriendo diccionario con for")
for key in dictionary.keys():
    print(key,"-->",dictionary[key])
for spanish,french in dictionary.items():
    print(spanish,"-->",french)
#como recorrer un diccionario con for
print("Modificando y añadiendo valores al diccionario")
dictionary['gato']='minou'#modifica
dictionary['gallina']='poulet'#añade
print(dictionary)
#las tuplas no se pueden modificar pero los diccionarios si
#mutables/inmutables
print("Imprimiendo el diccionario con for ordenado")
for key in sorted(dictionary.keys()):
    print(key,"-->",dictionary[key])#imprime de manera ordenada
print("Añadiendo al diccionario con update")
dictionary.update({"pato":"canard"})#otra manera de agregar al diccionario
print(dictionary)
print("Imprimiendo solo las claves del diccionario")
for french in dictionary.values():
    print(french)#imprimir valores
print("Eliminando valores del diccionario")
del dictionary['caballo']
print(dictionary)#elimina
print("Eliminar el ultimo elemento de la lista")
dictionary.popitem()
print(dictionary)
