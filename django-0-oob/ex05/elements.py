#!/usr/bin/python3
from elem import Text, Elem

class Html(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("html", attr, content)

class Head(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("head", attr, content)

class Body(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("body", attr, content)

class Title(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("title", attr, content)

class Meta(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("meta", attr, content, "simple")

class Img(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("img", attr, content, "simple")

class Table(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("table", attr, content)

class Th(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("th", attr, content)

class Tr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("tr", attr, content)

class Td(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("td", attr, content)

class Ul(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("ul", attr, content)

class Ol(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("ol", attr, content)

class Li(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("li", attr, content)

class H1(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("h1", attr, content)

class H2(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("h2", attr, content)

class P(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("p", attr, content)

class Div(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("div", attr, content)

class Span(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("span", attr, content)

class Hr(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("hr", attr, content)

class Br(Elem):
	def __init__(self, content=None, attr={}):
		super().__init__("br", attr, content)

def my_elements():
	print(Html())
	print(Head())
	print(Body())
	print(Title())
	print(Meta())
	print(Img())
	print(Table())
	print(Th())
	print(Tr())
	print(Td())
	print(Ul())
	print(Ol())
	print(Li())
	print(H1())
	print(H2())
	print(P())
	print(Div())
	print(Span())
	print(Hr())
	print(Br())

	print( Html( [Head(), Body()] ) )

	print(Html([
		Head(Title(Text( '"Hello ground!"' ))),
		Body([
			H1(Text('"Oh no, not again!"')),
			Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
		])
	]))

if __name__ == "__main__":
	my_elements()