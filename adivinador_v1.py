#@adivinador_v1.py
#importamos funciones aleatorias de la libreria estandar que se llama random
import random

#idea
#lista con elem.
#generar un no. aleatorio
#imprimir la entrada de la lista con indice obtenido en el paso 2
#funcion para saber cuantos elemntos tiene una lista -----length
#print(len(vec1))
#para importar de una libreria lo que ocupamos y sin ver otra cosa, ponemos importa random

elementos=["H","Li","Na","k","Rb","Cs","Fr","Be","Mg","Ca"]

#indice aleatorio y randint nos dice que son las variables que hay en todo el vector pero refiriendonos a la longitud de la lista
#randint te asigna un valor aleator de la lista o longitud del vectro
indice=random.randint(0,len(elementos)-1)
print(indice)
print(elementos[indice])