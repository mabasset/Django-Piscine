#!/usr/bin/python3
from elements import *

class Page:
	def __init__(self, elem: Elem):
		if not self.is_valid(elem):
			raise self.InvalidElem()
		self.elem = elem

	class InvalidElem(Exception):
		def __init__(self):
			super().__init__("Page: Invalid element")

	def __str__(self):
		if isinstance(self.elem, Html):
			return "<!DOCTYPE html>\n" + self.elem.__str__()
		return self.elem.__str__()

	def write_to_file(self, filename):
		with open(filename, 'w') as f:
			f.write(self.__str__())

	@staticmethod
	def is_valid(elem: Elem) -> bool:
		def recursion(elem):
			nonlocal validity
			if not validity or elem == [] or type(elem) == Text:
				return
			if type(elem) == list:
				for el in elem:
					recursion(el)
				return
			elif not isinstance(elem, (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td , Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)):
				validity = False
			elif not elem.is_valid():
				validity = False
			recursion(elem.content)

		validity = True
		recursion(elem)
		return validity

def my_page():
	test = {
		"invalid_type": Html([
			Head(Title(Text( '"Hello ground!"' ))),
			Body([
				H1(Text('"Oh no, not again!"')),
				Elem("ciao")
			])
		]),
		"missing_head": Html(Body()),
		"missing_body": Html(Head()),
		"wrong_order":  Html([
			Body(),
			Head()
		]),
		"multiple_title": Head([
			Title(Text( '"Hello ground!"' )),
			Title(Text( '"Hello ground!"' ))
		]),
		"invalid_type_div": Div(Img()),
		"invalid_type_body": Body(Meta()),
		"invalid_type_h1": H1(H1()),
		"invalid_type_p": P(H2()),
		"invalid_type_span": Span(Tr()),
		"invalid_type_ul": Ul(Th()),
		"invalid_type_ol": Ol(Td()),
		"missing_li": Ul(),
		"missing_th_td": Tr(),
		"not_mutual": Tr([
			Td(), Th()
		]),
		"invalid_type_table": (Table(Br()))
	}
	for k, v in test.items():
		print(k, ':', Page.is_valid(v))
	cv = Html([
		Head([
			Meta(attr={"charset": "UTF-8"}),
			Meta(attr={"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
			Title(Text("Matteo's CV"), {"style": "text-transform: capitalize;"})
		]),
		Body([
			H1(Text("Matteo's CV"), {"style": "text-transform: capitalize;"}),
			Ul([
				Li(),
				Li(),
			], {"style": "list-style: none; padding-left: 0;"}),
		])
	])

if __name__ == "__main__":
	my_page()