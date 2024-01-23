o=int(input("Ingresa un numero:"))
b=int(input("Ingresa otro numero"))
try:
    print(o/b)
except ZeroDivisionError:
    print("No se puede dividir entre 0")
except ValueError:
    print("Valor ingresado erroneo")
except TypeError:
    print("Esta excepción aparece cuando intentas aplicar un dato cuyo tipo no se puede aceptar en el contexto actual.")
except AttributeError:
    print("Esta excepción llega - entre otras ocasiones - cuando intentas activar un método que no existe en un elemento con el que se está tratando.")
except SyntaxError:
    print("Esta excepción se genera cuando el control llega a una línea de código que viola la gramática de Python. ")
    
