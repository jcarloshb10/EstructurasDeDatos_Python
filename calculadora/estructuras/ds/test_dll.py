from adt.lists.dll import DoublyLinkedList

if __name__ == "__main__":
	dll = DoublyLinkedList()
	print('e', dll.is_empty())

	dll.explorer()
	print('r 7', dll.remove(7))

	print('a 1', dll.append(1))
	print('a "2"', dll.append("2"))
	print('a 3', dll.append(3))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('e', dll.is_empty())

	print('i 0 0', dll.insert(0, 0))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('i 2 2', dll.insert(2, 2))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('i 4 4', dll.insert(4, 4))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('i "5" 5', dll.insert("5", 5))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('i 6 -3', dll.insert(6, -3))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('a 5', dll.append(5))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('r 5', dll.remove(5))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('r 2', dll.remove(2))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('r 0', dll.remove(0))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('r -5', dll.remove(-5))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('r 10', dll.remove(10))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('a 6', dll.append(6))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('i 7 4', dll.insert(7, 4))
	dll.explorer()
	print([i for i in dll], len(dll))

	dll = DoublyLinkedList()
	print('a "1"', dll.append('1'))
	print('a "1"', dll.append('1'))
	print('a "1"', dll.append('1'))
	print('a "2"', dll.append('2'))
	print('a "1"', dll.append('1'))
	print('a "2"', dll.append('2'))
	print('a "3"', dll.append('3'))
	print('a "1"', dll.append('1'))
	print('a "2"', dll.append('2'))
	print('a "3"', dll.append('3'))
	print('a 4', dll.append(4))
	print('a None', dll.append(None))
	print([i for i in dll], len(dll))

	print('d "1"', dll.delete('1'))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('d "2" all', dll.delete('2', all=True))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('d "4" all', dll.delete('4', all=True))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('d "1" all', dll.delete('1', all=True))
	dll.explorer()
	print([i for i in dll], len(dll))

	print('d "3" all', dll.delete('3', all=True))
	dll.explorer()
	print([i for i in dll], len(dll))

	for i in range(10):
		dll.append(i)
	print(dll, len(dll))
	dll.onward = False
	print(dll, len(dll))

	print(dll.forward())
	print(dll.forward())
	print(dll.forward())
	print(dll.forward())
	print(dll.forward())
	print(dll.forward())
	print(dll.forward())
	print(dll.backward())
	print(dll.backward())
	print(dll.backward())
	print(dll.backward())
	print(dll.forward())
	print(dll.forward())

	print('-------------------------')
	dll = DoublyLinkedList()
	print('a "1"', dll.append('1'))
	print('a "2"', dll.append('2'))
	print('a "3"', dll.append('3'))

	dll.explorer()
	for i in range(4):
		print(dll.forward())
	for i in range(4):
		print(dll.backward())
