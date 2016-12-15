class Producto(object):
	"""Clase Producto que sirve para instanciar un nuevo producto"""
	def __init__(self, nombre, cantidad, precio):
		self.__nombre = nombre
		self.__cantidad = cantidad
		self.__precio = precio

	@property
	def nombre(self):
		return self.__nombre

	@property
	def cantidad(self):
		return self.__cantidad

	@property
	def precio(self):
		return self.__precio

	@nombre.setter
	def nombre(self, nombre):
		self.__nombre = nombre

	@cantidad.setter
	def cantidad(self, cantidad):
		self.__cantidad = cantidad

	@precio.setter
	def precio(self, precio):
		self.__precio = precio

	#Aun no esta solucionado este metodo
	def resumen(self):
		return "Nombre: {} \n Cantidad: {} \n Precio: {}".format(nombre, cantidad, precio)