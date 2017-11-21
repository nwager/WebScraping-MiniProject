import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
import argparse
import pickle

# pip install -r requirements.txt for packages

# example: to skip scraping the temperature, type into CLI:
#     runwebscraper.py --skiptemp 5
# you have to type an integer with the command
# this tells the program to run every 'integer' seconds


def scrape():

	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('--skipperiod', action='store_true')
	parser.add_argument('--skipshort_desc', action='store_true')
	parser.add_argument('--skipdesc', action='store_true')
	parser.add_argument('--skiptemp', action='store_true')
	parser.add_argument('integer', type=int)
	parser.add_argument('numoftimes', type=int)
	args = parser.parse_args()

	print(args)

	periodChange = "none"
	short_descChange = "none"
	tempChange = "none"
	descChange = "none"

	numberOfScrapes = args.numoftimes;
	scrapeCounter = 0

	while True:

		page = requests.get("http://forecast.weather.gov/MapClick.php?lat=45.5118&lon=-122.6756#.WhHjyhOPJE4")
		soup = BeautifulSoup(page.content, 'html.parser')
		seven_day = soup.find(id="seven-day-forecast")
		forecast_items = seven_day.find_all(class_="tombstone-container")
		tonight = forecast_items[0]
		

		period_tags = seven_day.select(".tombstone-container .period-name")
		periods = [pt.get_text() for pt in period_tags]
		short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
		temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
		descs = [d["title"] for d in seven_day.select(".tombstone-container img")]


		# notify  if any values change, and don't notify
		# if a parameter is skipped
		if periodChange != periods and args.skipperiod == False:
			print "Time period changed to: " + str(periods)
			periodChange = periods

		if tempChange != temps and args.skiptemp == False:
			print "Temperature changed to: " + str(temps)
			tempChange = temps

		if descChange != descs and args.skipdesc == False:
			print "Long description changed to: " + str(descs)
			descChange = descs

		if short_descChange != short_descs and args.skipshort_desc == False:
			print "Short description changed to: " + str(short_descs)
			short_descChange = short_descs

		#print(short_descs)
		#print(temps)
		#print(descs)
		#print(periods)

		# check if any parameters were skipped
		if args.skipperiod == True:
			periods = "none"

		if args.skipshort_desc == True:
			short_descs = "none"

		if args.skiptemp == True:
			temps = "none"

		if args.skipdesc == True:
			descs = "none"

		# arrange data into panda table
		weather = pd.DataFrame({
		        "desc":descs, 
		        "short_desc": short_descs, 
		        "temp": temps,
		        "period": periods
		    })
		print(weather)

		scrapeCounter += 1

		if (scrapeCounter >=  numberOfScrapes):
			break

		if args.integer < 2:
			time.sleep(2)
		else:
			time.sleep(args.integer)



if __name__ == "__main__":
	scrape()
