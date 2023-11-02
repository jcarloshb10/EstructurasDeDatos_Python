from adt.lists.nodes import DoubleLinkedNode


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.nodo_actual = self.head
		self.__onward = True

	def is_empty(self):
		return self.head is None

	def append(self, data):
		new_node = DoubleLinkedNode(data)
		if self.is_empty():
			self.head = new_node
			self.nodo_actual = new_node
			return True
		elif isinstance(data, type(self.head.data)):
			nodo_actual = self.head
			while nodo_actual.next is not None:
				nodo_actual = nodo_actual.next

			nodo_actual.next = new_node
			new_node.preceding = nodo_actual
			return True
		return False

	def insert(self, data, pos):
		if isinstance(data, type(self.head.data)):
			new_node = DoubleLinkedNode(data)
			if pos == 0:
				new_node.next = self.head
				self.head.preceding = new_node
				self.head = new_node
				return True
			elif pos == len(self):
				return self.append(data)
			else:
				contador = 0
				nodo_actual = self.head
				while contador < pos:
					nodo_actual = nodo_actual.next
					contador += 1
				new_node.next = nodo_actual
				nodo_actual.preceding.next = new_node

				new_node.preceding = nodo_actual.preceding
				nodo_actual.preceding = new_node
				return True
		return False

	def remove(self, pos):
		if not self.is_empty():
			if pos == 0:
				self.head = self.head.next
				self.head.preceding = None
				return True

			elif pos > 0:
				nodo_actual = self.head
				contador = 0

				while nodo_actual:
					if contador == pos:
						if nodo_actual.preceding:
							nodo_actual.preceding.next = nodo_actual.next

						if nodo_actual.next:
							nodo_actual.next.preceding = nodo_actual.preceding
						return True

					nodo_actual = nodo_actual.next
					contador += 1
		return False

	def delete(self, data, all=False):
		eliminado = False
		if self.head.data == data:
			self.head = self.head.next
			if self.head == self.nodo_actual:
				self.nodo_actual = self.head
			eliminado = True
		else:
			nodo_actual = self.head
			while nodo_actual:
				if nodo_actual.data == data:
					nodo_actual.preceding.next = nodo_actual.next
					if nodo_actual.next:
						nodo_actual.next.preceding = nodo_actual.preceding
					if nodo_actual == self.nodo_actual:
						self.nodo_actual = nodo_actual.preceding
					eliminado = True
				nodo_actual = nodo_actual.next

		if all and self.search(data):
			return self.delete(data, all)
		return eliminado

	def search(self, data):
		if not self.is_empty():
			nodo_actual = self.head
			while nodo_actual is not None:
				if data == nodo_actual.data:
					return nodo_actual.data
				nodo_actual = nodo_actual.next
		return None

	def locate(self, pos):
		contador = 0
		if not self.is_empty():
			nodo_actual = self.head
			while nodo_actual is not None:
				if contador == pos:
					return nodo_actual.data
				contador += 1
				nodo_actual = nodo_actual.next
		return None

	def forward(self):
		if self.nodo_actual.next is not None:
			self.nodo_actual = self.nodo_actual.next
		return self.nodo_actual.data

	def backward(self):
		if self.nodo_actual.preceding is not None:
			self.nodo_actual = self.nodo_actual.preceding
		return self.nodo_actual.data

	@property
	def onward(self):
		return self.__onward

	@onward.setter
	def onward(self, onward):
		self.__onward = onward

	def explorer(self):
		if not self.is_empty():
			nodo_actual = self.head
			while nodo_actual is not None:
				print(nodo_actual.data)
				nodo_actual = nodo_actual.next

	def __str__(self):
		cadena = ''
		if not self.is_empty():
			if self.onward == True:
				nodo_actual = self.head

				while nodo_actual is not None:
					cadena = cadena + str(nodo_actual.data)
					cadena = cadena + '\n'
					nodo_actual = nodo_actual.next
			else:
				nodo_actual = self.head
				while nodo_actual.next is not None:
					nodo_actual = nodo_actual.next
				
				while nodo_actual is not None:
					cadena = cadena + str(nodo_actual.data)
					cadena = cadena + '\n'
					nodo_actual = nodo_actual.preceding
		return cadena

	def __len__(self):
		contador = 0
		if not self.is_empty():
			nodo_actual = self.head
			while nodo_actual is not None:
				contador += 1
				nodo_actual = nodo_actual.next
		return contador

	def __iter__(self):
		if not self.is_empty():
			nodo_actual = self.head
			while nodo_actual is not None:
				yield nodo_actual.data
				nodo_actual = nodo_actual.next
