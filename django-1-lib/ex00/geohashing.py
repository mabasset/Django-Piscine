#!/usr/bin/python3

import sys, antigravity

def my_geohashing():
	if (len(sys.argv) != 5):
		print("Latitude[float], longitude[float], date[y-m-d] and Dow Jones opening[float] required as arguments")
		sys.exit(1)
	try:
		latitude = float(sys.argv[1])
		longitude = float(sys.argv[2])
		date = f'{sys.argv[3]}-{sys.argv[4]}'.encode()
		antigravity.geohash(latitude, longitude, date)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	my_geohashing()