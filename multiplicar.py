# Solicitar al usuario un número del 1 al 12 y validar que sea un número
while True:
    try:
        numero = int(input("Por favor, ingresa un número del 1 al 12: "))
        if 1 <= numero <= 12:
            break  # El número es válido, salimos del bucle
        else:
            print("El número debe estar en el rango del 1 al 12. Intenta de nuevo.")
    except ValueError:
        print("Debes ingresar un número válido.")

# Imprimir la tabla de multiplicar
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
