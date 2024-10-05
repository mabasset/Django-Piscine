import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

def my_machine():
	class CoffeeMachine():
		def __init__(self):
			self.servings = 0
		class EmptyCup(HotBeverage):
			def __init__(self):
				self.name = "empty cup"
				self.price = 0.90
			def description(self):
				return "An empty cup?! Gimme my money back!"
		class BrokenMachineException(Exception):
			def __init__(self):
				super().__init__("This coffee machine has to be repaired.")
		def repair(self):
			print("Coffee machine under maintence...")
			self.servings = 0
		def serve(self, BeverageClass: HotBeverage) -> HotBeverage:
			if (self.servings == 10):
				raise self.BrokenMachineException()
			self.servings += 1
			if random.random() > 0.2:
				return BeverageClass()
			return self.EmptyCup()
	
	machine = CoffeeMachine()
	for i in range(22):
		try:
			beverage = machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
			print(i, beverage)
		except CoffeeMachine.BrokenMachineException as e:
			print(e)
			machine.repair()

if __name__ == "__main__":
	my_machine()
	