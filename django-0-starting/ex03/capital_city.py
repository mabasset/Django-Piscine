#!/usr/bin/python3
import sys

def my_capital_city(argv):
	if len(argv) != 2:
		sys.exit(1)
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	try:
		print(capital_cities[states[argv[1]]])
	except:
		print("Unknown state")
	

if __name__ == "__main__":
	my_capital_city(sys.argv)