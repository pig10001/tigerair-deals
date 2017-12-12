import urllib2
import json
import sys
import argparse

def main(arg):

	dump = urllib2.urlopen("https://tigerair.com.au/api/fare_proposals.json?origin=&destination=&order=&travel=&pushlish_on=&preview=&page_type=standard&fare_type=Tactical&route=false").read()
	deals = json.loads(dump)

	deal_dict = {}

	for deal in deals:
		origin_name = deal["origin"]["name"]
		destination_name = deal["destination"]["name"]
		if origin_name in deal_dict:
			deal_dict[origin_name].append(destination_name)
		else:
			deal_dict[origin_name] = [destination_name]

	print deal_dict[vars(arg)["origin"]]


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('--origin')
	main(parser.parse_args())
