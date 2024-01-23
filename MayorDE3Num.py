# Se leen tres números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))


if number1 > number2 and number1 > number3: largest_number = number1

elif number2 > number1 and number2 > number3: largest_number = number2


elif number3 > number2 and number3 > number1:largest_number = number3

elif number1 == number2 or number1 == number3: largest_number=number1; print("Dos numeros con el mismo valor detectados");

elif number2 == number3: largest_number=number2; print("Dos numeros con el mismo valor detectados");

elif number1 == number2 and number1 == number3: largest_number=number1; print("Todos los numeros tienen el mismo valor");

else:print("ERROR"); 


# Imprime el resultado.
print("El número más grande es:", largest_number)







