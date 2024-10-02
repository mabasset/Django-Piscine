import sys

def my_periodic_table(argv):
	def parse_file():
		def convert_value(value):
			try:
				return int(value)
			except:
				return value

		with open(argv[1], 'r') as f:
			for line in f.read().split('\n'):
				if line:
					element = {k.strip(): convert_value(v.strip()) for k, v in (item.strip().split(':') for item in line.split("=")[1].strip().split(','))}
					element["name"] = line.split("=")[0].strip()
					el_list.append(element)
		el_list.sort(key=lambda el: int(el["number"]))

	def generate_html():
		row_length = max([element["position"] for element in el_list]) + 1
		html = '<!DOCTYPE html>\n<html lang="en">\n\t<head>\n\t\t<meta charset="UTF-8">\n\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\t<title>Periodic Table</title>\n\t</head>\n\t<body>\n\t\t<table style="table-layout: fixed; border-collapse: collapse; width: 100%; text-align: center;">\n\t\t'
		while el_list:
			html += '\t<tr>\n\t\t\t'
			for i in range(row_length):
				if i == el_list[0]["position"]:
					html += f'\t<td style="border: 2px black solid;">\n\t\t\t\t\t<h4>{el_list[0]["name"]}</h4>\n\t\t\t\t\t<ul style="list-style-type: none; padding: 0;">\n\t\t\t\t\t\t<li>{el_list[0]["number"]}</li>\n\t\t\t\t\t\t<li>{el_list[0]["small"]}</li>\n\t\t\t\t\t\t<li>{el_list[0]["molar"]}</li>\n\t\t\t\t\t</ul>'
					el_list.pop(0)
				else:
					html += '\t<td>'
				html += '\n\t\t\t\t</td>\n\t\t\t'
				print(i)
			html += '</tr>\n\t\t'
		html += '</table>\n\t</body>\n</html>'
		return html

	if len(argv) != 2:
		sys.exit(1)
	el_list = []
	parse_file()
	html = generate_html()
	print(html)
	with open("./my_periodic_table.html", 'w') as f:
		f.write(html)

if __name__ == '__main__':
	my_periodic_table(sys.argv)
