import os


def read(path):
	string = ''
	with open(path) as file:
		for i in file:
			string += i
	return string


def separate_lines(string):
	aux = ''
	_list = []
	for i in string:
		if i == '\n':
			_list.append(aux)
			aux = ''
		else:
			aux += i
	return _list


def write(path, string):
	with open(path, 'w') as file:
		file.write(string)


def append(path, string):
	if os.path.exists(path):
		with open(path, 'a') as file:
			file.write(string + '\n')
	else:
		write(path, string)


if __name__ == '__main__':
	path = input('File name: ')
	string = read(path)
	string = string.replace('	    ', '\t')
	write(path, '')
	for i in separate_lines(string):
		append(path, i)
	print('finished...')
