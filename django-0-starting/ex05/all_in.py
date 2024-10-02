import sys

def my_all_in(argv):
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

	def my_capital_city(state):
		try:
			print(capital_cities[states[state]], "is the capital of", state)
			return True
		except:
			return False
	def my_state(city):
		try:
			acronym = list(capital_cities.keys())[list(capital_cities.values()).index(city)]
			print(city, "is the capital of", list(states.keys())[list(states.values()).index(acronym)])
			return True
		except:
			return False

	for item in argv[1].split(", "):
		if not item or ( my_capital_city(item.title()) or my_state(item.title()) ):
			continue
		print(item, "is neither a capital city nor a state")


if __name__ == "__main__":
	my_all_in(sys.argv)