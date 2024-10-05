#!/usr/bin/python3
import sys, os, re

def my_render(template_file, settings_file):
	settings_dict = {}
	for line in settings_file:
		key, value = line.strip().split('=')
		settings_dict[key.strip(' "')] = value.strip(' "')
	html = template_file.read().format(**settings_dict)
	with open(sys.argv[1].replace(".template", ".html"), 'w') as f:
		f.write(html)

if __name__ == "__main__":
	if len(sys.argv) != 2 or not sys.argv[1].endswith(".template"):
		sys.exit(1)
	try:
		with open(sys.argv[1], 'r') as f:
			with open("./settings.py") as s:
				my_render(f, s)
	except:
		sys.exit(1)