from adt.lists.cll import CircularLinkedList

if __name__ == "__main__":
	cll = CircularLinkedList()
	print("is empty", cll.is_empty())

	print("r 2", cll.remove(2))
	cll.explorer()

	print('a 5', cll.append(5))
	print('a 8', cll.append(8))
	cll.append("h")

	print("is empty", cll.is_empty())
	cll.explorer()

	print("i 0 0", cll.insert(0, 0))
	cll.explorer()
	print("i 9 3", cll.insert(9, 3))
	cll.explorer()
	print("i 18 2", cll.insert(18, 2))
	cll.explorer()
	print("i 'h' 2", cll.insert("h", 2))
	cll.explorer()
	print("i 3 18", cll.insert(3, 18))
	cll.explorer()
	print("i 1 -1", cll.insert(1, -1))
	cll.explorer()

	print('a 10', cll.append(10))

	print("r 5", cll.remove(5))
	cll.explorer()

	print("r 0", cll.remove(0))
	cll.explorer()

	print("r -2", cll.remove(-2))
	cll.explorer()

	print("r 12", cll.remove(12))
	cll.explorer()

	cll = CircularLinkedList()
	cll.append(1)
	cll.append(2)
	cll.append(3)
	cll.append(3)
	cll.append(4)
	cll.append(5)
	cll.explorer()

	print("d 1", cll.delete(1))
	cll.explorer()

	print("d 5", cll.delete(5))
	cll.explorer()

	print("d 3", cll.delete(3))
	cll.explorer()

	print("d 9", cll.delete(9))
	cll.explorer()

	cll = CircularLinkedList()
	cll.append(1)
	cll.append(2)
	cll.append(3)
	cll.append(4)
	cll.append(5)
	cll.append(3)
	cll.append(2)
	cll.append(3)
	cll.append(4)
	cll.append(5)
	cll.explorer()

	print("d 1", cll.delete(1, True))
	cll.explorer()

	print("d 5", cll.delete(5, True))
	cll.explorer()

	print("d 3", cll.delete(3, True))
	cll.explorer()

	print("d 9", cll.delete(9, True))
	cll.explorer()

	cll = CircularLinkedList()
	cll.append(1)
	cll.append(2)
	cll.append(3)
	cll.append(4)
	cll.append(5)
	cll.explorer()

	print(cll.roulette(0))
	print(cll.roulette(2))
	print(cll.roulette(4))
	print(cll.roulette(10))
	print(cll.roulette(-3))

	print(".", end="")

	cll = CircularLinkedList()

	print(cll.insert(30, 1))
	cll.explorer()
