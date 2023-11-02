class Estudiante:
	def __init__(self, codigo, nombre, nota):
		self.codigo = codigo
		self.nombre = nombre
		self.nota = nota

	def __str__(self):
		print(f'codigo={self.codigo}, nombre={self.nombre}, nota={self.nota}')

