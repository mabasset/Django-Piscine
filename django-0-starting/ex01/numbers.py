#!/usr/bin/python3
def my_numbers(filename):
	with open(filename, 'r') as f:
		for nbr in f.read().split(','):
			print(int(nbr))

if __name__ == '__main__':
	my_numbers("../d01/ex01/numbers.txt")
