from path import Path

def my_program():
	Path.makedirs("dir")
	f = Path("dir/file.txt")
	f.write_text("ciao!")
	print(f.read_text())

if __name__ == "__main__":
	my_program()