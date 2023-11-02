from adt.lists.nodes import SinglyLinkedNode


class CircularLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def is_empty(self):
		return self.head is None

	def append(self, data):
		if self.is_empty():
			self.head = SinglyLinkedNode(data)
			self.tail = self.head
			nuevo_nodo.next = self.head
			return True
		elif isinstance(data, type(self.head.data)):
			self.tail.next = SinglyLinkedNode(data)
			self.tail.next.next = self.head
			self.tail = self.tail.next
			return True
		return False

	def insert(self, data, rel_pos):
		nuevo_nodo = SinglyLinkedNode(data)

		if self.is_empty():
			if rel_pos == 0:
				return self.append(data)
		elif isinstance(data, type(self.head.data)):
			if rel_pos == 0:
				nuevo_nodo.next = self.head
				self.head = nuevo_nodo
				self.tail.next = nuevo_nodo
				return True

			elif rel_pos == len(self):
				return self.append(data)

			elif rel_pos > 0:
				nodo_actual = self.head
				i = 0
				while i < rel_pos - 1:
					i += 1
					nodo_actual = nodo_actual.next
				nodo_auxiliar = nodo_actual.next
				nodo_actual.next = nuevo_nodo
				nuevo_nodo.next = nodo_auxiliar

				return True
		return False

	def remove(self, rel_pos):
		if not self.is_empty():
			if rel_pos == 0:
				self.head = self.head.next
				self.tail.next = self.head
				return True
			elif rel_pos > 0:
				nodo_actual = self.head
				contador = 0
				while contador < rel_pos - 1:
					nodo_actual = nodo_actual.next
					contador += 1

				if rel_pos == len(self) - 1:
					self.tail = nodo_actual

				nodo_actual.next = nodo_actual.next.next
				self.tail.next = self.head
				return True
		return False

	def delete(self, data, all=False):
		if not self.is_empty():
			if self.head.data == data:
				self.head = self.head.next
				self.tail.next = self.head
				return True
			else:
				nodo_actual = self.head
				while True:
					if nodo_actual.next.data == data:

						if nodo_actual.next == self.tail:
							self.tail = nodo_actual
						nodo_actual.next = nodo_actual.next.next
						self.tail.next = self.head

						return True
					nodo_actual = nodo_actual.next
					if nodo_actual == self.head:
						if not all and self.search(data) is not None:
							break
		return False

	def search(self, data):
		if not self.is_empty():
			if data == self.head.data:
				return self.head.data
			nodo_actual = self.head.next
			while nodo_actual != self.head:
				if data == nodo_actual.data:
					return nodo_actual.data
				nodo_actual = nodo_actual.next

	def roulette(self, rel_pos):
		if rel_pos > -1:
			contador = 0
			nodo_actual = self.head
			while contador < rel_pos:
				nodo_actual = nodo_actual.next
				contador += 1
			return nodo_actual.data
		return None

	def explorer(self):
		if not self.is_empty():
			print(self.head.data)
			nodo_actual = self.head.next
			while nodo_actual != self.head:
				print(nodo_actual.data)
				nodo_actual = nodo_actual.next

	def __str__(self):
		cadena = ""
		if not self.is_empty():
			cadena = cadena + str(self.head.data)
			cadena = cadena + '\n'
			nodo_actual = self.head.next
			while nodo_actual != self.head:
				cadena = cadena + str(nodo_actual.data)
				cadena = cadena + '\n'
				nodo_actual = nodo_actual.next
		return cadena

	def __len__(self):
		contador = 0
		if not self.is_empty():
			contador += 1
			nodo_actual = self.head.next
			while nodo_actual != self.head:
				contador += 1
				nodo_actual = nodo_actual.next
		return contador
		

	def __iter__(self):
		if not self.is_empty():
			yield self.head.data
			nodo_actual = self.head.next
			while nodo_actual != self.head:
				yield nodo_actual.data
				nodo_actual = nodo_actual.next
