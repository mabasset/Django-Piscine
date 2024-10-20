import sys, requests
from bs4 import BeautifulSoup

def main():
	if len(sys.argv) != 2:
		sys.exit("argument error")
	titles = [sys.argv[1]]
	try:
		while titles[-1].lower() != "philosophy":
			if any(titles.count(x) > 1 for x in titles):
				raise Exception("It leads to an infinite loop !")
			response = requests.get(f'https://en.wikipedia.org/wiki/{titles[-1]}')
			response.raise_for_status()
			print(titles[-1])
			soup = BeautifulSoup(response.text, "html.parser")
			for sup in soup.find_all("sup"):
				sup.decompose()
			new_title = None
			for p in soup.find_all('p'):
				a = p.find('a')
				if not a or not a.has_attr('title'):
					continue
				new_title = a.get("title")
				break
			if not new_title:
				raise requests.exceptions.HTTPError
			titles.append(new_title)
		print("Philosophy")
		print(f'{len(titles)} roads from {titles[0]} to philosophy !')
	except requests.exceptions.HTTPError:
		print("It leads to a dead end !")
		sys.exit(1)
	except requests.exceptions.ConnectionError:
		print("Connection error !")
		sys.exit(1)
	except Exception as e:
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	main()