#!/usr/bin/python3
import sys

def my_periodic_table(argv):
	def parse_line(line):
		def convert_value(value):
			try:
				return int(value)
			except:
				return value

		element = {k.strip(): convert_value(v.strip()) for k, v in (item.strip().split(':') for item in line.split("=")[1].strip().split(','))}
		element["name"] = line.split("=")[0].strip()
		return element

	def generate_html(el_list):
		html = """<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<title>CV</title>
	</head>
	<body>
		<table style="table-layout: fixed; border-collapse: collapse; width: 100%; text-align: center;">{}
		</table>
	</body>
</html>"""
		box_template = """
				<td style="border: 2px black solid;">
					<h4>{}</h4>
					<ul style="list-style-type: none; padding: 0;">
						<li>No {}</li>
						<li>{}</li>
						<li>{}</li>
					</ul>"""

		row_length = max([element["position"] for element in el_list]) + 1
		table_body = ""
		while el_list:
			table_body += '\n\t\t\t<tr>'
			for i in range(row_length):
				el = el_list[0]
				if i == el["position"]:
					table_body += box_template.format(el["name"], el["number"], el["small"], el["molar"])
					el_list.pop(0)
				else:
					table_body += '\n\t\t\t\t<td>'
				table_body += '\n\t\t\t\t</td>'
			table_body += '\n\t\t\t</tr>'
		return html.format(table_body)

	if len(argv) != 2:
		sys.exit(1)
	f = open(argv[1], 'r')
	el_list = [parse_line(line.strip()) for line in f]
	f.close()
	html = generate_html(sorted(el_list, key=lambda el: el["number"]))
	with open("./my_periodic_table.html", 'w') as f:
		f.write(html)

if __name__ == '__main__':
	my_periodic_table(sys.argv)
