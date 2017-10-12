import random
# iteradores.py
#repaso
#salida de datos es con la funcion print
#nombre= input("dime..") de esta forma metemos alguna cadena de texto que se guarda como variable
#print("hola")
#para correr un programa ponemos en el sistema de equipo python (espacio) y sigue el nombre del archivo  que guardamos como archivo .py

vec1=[8,2,1]
print(vec1)
#indexacion  comienza a buscar el elemento del vector comezando con 0 luego 1, 2...n
print(vec1[1])
#para cambiar alguno de los valores del vector ponemos vec[2]=1.5
vec1[2]=1.5
print(vec1)
#para añadir un valor mas al vector pondremos append
vec1.append(10)
print(vec1)

#tupla es una lista que se guarda para ya no modificar nada
tupla=(3,2)
print(tupla)
#tupla[3]=42
#print(tupla)

#lista con elem.
#generar un no. aleatorio
#imprimir la entrada de la lista con indice obtenido en el paso 2
#funcion para saber cuantos elemntos tiene una lista -----length
print(len(vec1))
#para importar de una libreria lo que ocupamos y sin ver otra cosa, ponemos importa random