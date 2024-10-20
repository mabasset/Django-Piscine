import requests, dewiki, json, sys

def main():
	content = ""
	try:
		if len(sys.argv) != 2 or not sys.argv[1]:
			raise(Exception("argument error"))
		endpoint = "https://fr.wikipedia.org/w/api.php"
		params = {
			"action": "parse",
			"page": sys.argv[1].title(),
			"prop": "wikitext",
			"format": "json",
			"redirects": "true"
		}
		response = requests.get(endpoint, params)
		response.raise_for_status()
		content = json.loads(response.text)
		if content.get("error") is not None:
			raise Exception(content["error"]["info"])
		with open(f'{sys.argv[1].replace(" ", "_").lower()}.wiki', "w") as f:
			f.write(dewiki.from_string(content["parse"]["wikitext"]["*"]))
	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()