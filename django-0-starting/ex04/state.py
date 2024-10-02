#!/usr/bin/python3
import sys

def my_state(argv):
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
		acronym = list(capital_cities.keys())[list(capital_cities.values()).index(argv[1])]
		print(list(states.keys())[list(states.values()).index(acronym)])
	except:
		print("Unknown capital city")

if __name__ == "__main__":
	my_state(sys.argv)
