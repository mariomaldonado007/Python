#   Convertidor de unidades

# Funciones a usar 
def Sistema_de_unided():
	print("Introduce sistema de unidades:")
	print("a) Sistema ingles")
	print("b) Sistema internacional")

	respuesta = input("Ingresa tu respuesta > ")
	if respuesta == "a" or  respuesta == "A":
		sistema = "Ingles"
	elif respuesta == "b" or  respuesta == "B":
		sistema = "internacional"
	else :
		print ("Estas muy wey, suerte para la proxima novato")	
		sistema = None
	return sistema


def Magnitud_o_Unidad_fundamental():
	print("Introduce sistema de unidades:")
	print("a) Magnitud")
	print("b) Unidad fundamental")

	respuesta = input("Ingresa tu respuesta > ")
	if respuesta == "a" or  respuesta == "A":
		meco = "magnitud"
	elif respuesta == "b" or  respuesta == "B":
		meco = "unidad fundamental"
	else :
		print ("Estas muy wey, suerte para la proxima novato")	
		meco = "error"
	return meco


# Programa principal
sis = Sistema_de_unided()
print("Sistema escogido: ", sis)
print()

cosa = Magnitud_o_Unidad_fundamental()
print("Meco = ", cosa)