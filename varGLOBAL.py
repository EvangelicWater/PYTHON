def my_function():
    global var
    var = 2
    print("Variable original", var)


var = 1
my_function()
print("Segunda llamada",var)
#la variable global no cambia su contenido 


def funcion():
    a=1
    print("Variable original:",a);

a=2
funcion()
print("Segunda llamada",a);

#la variable normal si cambia su contenido al llamarla fuera de la funcion
