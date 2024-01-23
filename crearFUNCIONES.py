def message():print("Ingresar valor: ");

print("Inicia aqui.")
message()
m=int(input())
print("Termina aqui.")
print(m,"fue el valor ingresado")

def hello(name):print("Hello,", name)    # cuerpo de la función
message

name = input("Ingresa tu nombre: ")

hello(name)    # invocación de la función

def call(char):print("Cadena:",char);
char=input("Ingresa una cadena:");
call(char);

def introduction(first_name, last_name):print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


def adding(a, b, c):print(a, "+", b, "+", c, "=", a + b + c)

adding(1, 2, 3);


def happy_new_year(wishes=False):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return print("Feliz año nuevo")
    wishes=True;
    
happy_new_year();



