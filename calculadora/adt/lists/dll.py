from adt.lists.nodes import DoubleLinkedNode


class DoublyLinkedList:
	def __init__(self) -> None:
		self.head = None
		self.__onward = True
		self.current_node = None

	@property
	def onward(self) -> bool:
		return self.__onward

	@onward.setter
	def onward(self, value) -> None:
		if isinstance(value, bool):
			self.__onward = value

	# @onward.deleter
	# def onward(self):
	#	 del self.__onward

	def is_empty(self) -> bool:
		return self.head == None

	def __tail(self) -> object:
		current_node = self.head
		while current_node.next:
			current_node = current_node.next
		return current_node

	def append(self, data) -> bool:
		new_node = DoubleLinkedNode(data)
		if self.is_empty():
			self.head = new_node
			self.current_node = self.head
		elif type(data) == type(self.head.data):
			tail = self.__tail()
			tail.next = new_node
			new_node.previous = tail
		else:
			return False
		return True

	def insert(self, data, pos) -> bool:
		if self.is_empty():
			if pos == 0:
				return self.append(data)
		elif type(data) == type(self.head.data):
			new_node = DoubleLinkedNode(data)
			if pos == 0:
				new_node.next = self.head
				self.head.previous = new_node
				self.head = new_node
				return True
			elif pos == len(self):
				return self.append(data)
			else:
				cnt = 0
				current_node = self.head
				while current_node:
					if cnt == pos:
						new_node.next = current_node
						new_node.previous = current_node.previous

						current_node.previous.next = new_node
						current_node.previous = new_node
						return True
					current_node = current_node.next
					cnt += 1
		return False

	def remove(self, pos) -> bool:
		if not self.is_empty():
			return self.delete(self.locate(pos))
		# 	if pos == 0:
		# 		self.head = self.head.next
		# 		self.head.previous = None
		# 		return True
		# 	elif pos > 0:
		# 		current_node = self.head
		# 		cnt = 0
		# 		while current_node:
		# 			if cnt == pos:
		# 				if current_node.previous:
		# 					current_node.previous.next = current_node.next
		# 				if current_node.next:
		# 					current_node.next.previous = current_node.previous
		# 				return True
		# 			current_node = current_node.next
		# 			cnt += 1
		# return False

	def delete(self, data, all=False) -> bool:
		deleted = False
		if self.head.data == data:
			if self.head == self.current_node:
				self.current_node = self.head.next
			self.head = self.head.next
			deleted = True
		else:
			current_node = self.head
			while current_node:
				if current_node.data == data:
					current_node.previous.next = current_node.next
					if current_node.next:
						current_node.next.previous = current_node.previous
					if current_node == self.current_node:
						self.current_node = current_node.previous
					deleted = True
				current_node = current_node.next

		if all and self.search(data):
			deleted = self.delete(data, all)
		return deleted

	def search(self, data) -> object:
		for i in self:
			if i == data:
				return i

	def locate(self, pos) -> object:
		cnt = 0
		for i in self:
			if cnt == pos:
				return i
			cnt += 1

	def forward(self) -> object:
		if self.current_node.next:
			self.current_node = self.current_node.next
		return self.current_node.data

	def backward(self) -> object:
		if self.current_node.previous:
			self.current_node = self.current_node.previous
		return self.current_node.data

	def explorer(self) -> None:
		print(self)

	def __str__(self) -> str:
		string = ''
		if not self.is_empty():
			current_node = self.head if self.onward else self.__tail()
			while current_node:
				string += str(current_node.data) + '\n'
				if self.onward:
					current_node = current_node.next
				else:
					current_node = current_node.previous
		return string

	def __len__(self) -> int:
		cnt = 0
		for _ in self:
			cnt += 1
		return cnt

	def __iter__(self) -> object:
		if not self.is_empty():
			current_node = self.head
			while current_node:
				yield current_node.data
				current_node = current_node.next
