from adt.lists.nodes import SinglyLinkedNode


class CircularLinkedList:
	def __init__(self) -> None:
		self.head = None
		self.tail = None

	def is_empty(self) -> bool:
		return self.head == None

	def append(self, data) -> bool:
		new_node = SinglyLinkedNode(data)
		if self.is_empty():
			self.head = new_node
			self.tail = new_node
			new_node.next = self.head
		elif type(data) == type(self.head.data):
			self.tail.next = new_node
			new_node.next = self.head
			self.tail = new_node
		else:
			return False
		return True

	def insert(self, data, rel_pos) -> bool:
		if self.is_empty():
			if rel_pos == 0:
				return self.append(data)
		elif type(data) == type(self.head.data):
			new_node = SinglyLinkedNode(data)
			if rel_pos == 0:
				new_node.next = self.head
				self.head = new_node
				self.tail.next = new_node
				return True
			elif rel_pos == len(self):
				return self.append(data)
			elif rel_pos > 0:
				current_node = self.head
				i = 0
				while i < rel_pos - 1:
					i += 1
					current_node = current_node.next
				current_node.next, new_node.next = new_node, current_node.next
				return True
		return False

	def remove(self, rel_pos) -> bool:
		if not self.is_empty():
			return self.delete(self.roulette(rel_pos))
		# 	aux = rel_pos
		# 	while aux >= len(self):
		# 		aux -= len(self)
		#
		# 	if rel_pos == 0 or aux == 0:
		# 		self.head = self.head.next
		# 		self.tail.next = self.head
		# 		return True
		#
		# 	elif rel_pos > 0:
		# 		current_node = self.head
		# 		cont = 0
		# 		while cont < rel_pos - 1:
		# 			current_node = current_node.next
		# 			cont += 1
		#
		# 		if rel_pos == len(self) - 1:
		# 			self.tail = current_node
		#
		# 		current_node.next = current_node.next.next
		# 		self.tail.next = self.head
		# 		return True
		# return False

	def delete(self, data, all=False) -> bool:
		deleted = False
		if not self.is_empty():

			if self.head.data == data:
				self.head = self.head.next
				self.tail.next = self.head
				deleted = True
			else:
				current_node = self.head
				while True:
					if current_node.next.data == data:

						if current_node.next == self.tail:
							self.tail = current_node
						current_node.next = current_node.next.next
						self.tail.next = self.head

						deleted = True
					current_node = current_node.next
					if current_node == self.head:
						break
		if all and self.search(data):
			deleted = self.delete(data, all)
		return deleted

	def search(self, data) -> object:
		for i in self:
			if i == data:
				return i

	def roulette(self, rel_pos) -> object:
		if rel_pos >= 0:
			cnt = 0
			current_node = self.head
			while cnt < rel_pos:
				current_node = current_node.next
				cnt += 1
			return current_node.data

	def explorer(self) -> None:
		print(self)

	def __str__(self) -> str:
		string = ""
		for i in self:
			string += str(i) + "\n"
		return string

	def __len__(self) -> int:
		cnt = 0
		for _ in self:
			cnt += 1
		return cnt

	def __iter__(self) -> object:
		if not self.is_empty():
			yield self.head.data
			current_node = self.head.next
			while current_node != self.head:
				yield current_node.data
				current_node = current_node.next
