# WebScraping-MiniProject
My runwebscraper.py and requirements.txt files.
These files are meant for a CLI.

Before running the .py file, type "pip install -r requirements.txt" to download the required packages for scraping.

The .py file scrapes the Portland weather forecast from forecast.weather.gov and gets the high and low temperatures, time period, short description, and long description.

To run the file, type "runwebscraper.py 5". The  "5" can be any number, but has to be included. It is the amount of seconds in between each scrape. To skip any of the 4 parameters, type after runwebscraper.py:

  --skipperiod (skip time period)
  
  --skiptemp (skip temperatures)
  
  --skipdesc (skip long description)
  
  --skipshort_desc (skip short description)

The program prints changes if it detects any. It also arranges all the data in a pandas table (pandas.DataFrame).
