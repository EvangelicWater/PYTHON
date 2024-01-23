"""
    programa realizado por: 
    - Diego Rodolfo Vargas Vega
    - Kevin Leopoldo Navarro Mercado
    - Andrés Humberto Martínez Escobedo   
"""

import random

#clase de flores 
class Flores: 
    
    #declaramos los atributos de la clase
    def __init__(self, flores, par):
        self.flores = flores
        self.par = par

    #metodo de generar poblacion
    def generar_poblacion(self):
            self.flores = []
            for i in range(100):
                self.flores.append(random.choice(['blanco', 'rojo']))
            return self.flores
    
    #metodo de elegir pares
    def elegir_pares(self):
            self.par = []
            for i in range(50):
                self.par.append(random.sample(self.flores, 2))
            return self.par
    
    #metodo de cruzar pares  
    def cruzar_pares(self):
        self.hijos = []
        for i in range(50):
            if self.par[i][0] == 'blanco' and self.par[i][1] == 'blanco':
                self.hijos.append('blanco')
            elif self.par[i][0] == 'rojo' and self.par[i][1] == 'rojo':
                self.hijos.append('rojo')
            else:
                self.hijos.append('blanco')
        return self.hijos
    
    #metodo de mutacion       
    def mutacion(self):
        self.mutacion = []
        for i in range(50):
            if self.hijos[i] == 'rojo':
                self.mutacion.append('rojo')
            else:
                if random.random() < 0.2:
                    self.mutacion.append('amarillo')
                else:
                    self.mutacion.append('blanco')
        return self.mutacion
    #metodo que imprime los resultados 
    def resultados(self):
        self.blanco = 0
        self.rojo = 0
        self.amarillo = 0
        for i in range(50):
            if self.mutacion[i] == 'blanco':
                self.blanco += 1
            elif self.mutacion[i] == 'rojo':
                self.rojo += 1
            else:
                self.amarillo += 1
        print('Total de flores hijas blancas: ', self.blanco)
        print('Total de flores hijas rojas: ', self.rojo)
        print('Total de flores hijas amarillas: ', self.amarillo)
   
#funcion principal para imprimir el menu        
def main():
    flores = Flores(0, 0)
    flores.generar_poblacion()
    while True:
        print("\n\t\t\t ALGORITMOS EVOLUTIVOS \n\t\t")
        print('\t\t\t [1] Generar poblacion\n')
        print('\t\t\t [2] Elegir pares\n')
        print('\t\t\t [3] Cruzar pares\n')
        print('\t\t\t [4] Mutacion\n')
        print('\t\t\t [5] Resultados\n')
        print('\t\t\t [6] Salir\n')
        opcion = int(input('Ingrese una opcion: '))
        print('\n')
        if opcion == 1:
            flores.generar_poblacion()
            print('\n poblacion generada con exito \n')
        elif opcion == 2:
            flores.elegir_pares()
            print('\n se han elegido pares con exito \n')
        elif opcion == 3:
            flores.cruzar_pares()
            print('\n se han cruzado los pares con exito \n')
        elif opcion == 4:
            flores.mutacion()
            print('\n mutacion generada con exito \n')
        elif opcion == 5:
            flores.resultados()
        elif opcion == 6:
            print(' Saliendo del programa')
            break
        else:
            print('Opcion invalida')

#llamado a la función main
if __name__ == '__main__':
    main()
            
            

