# WebScraping-MiniProject
My runwebscraper.py and requirements.txt files. These files are meant for a CLI.

First, install the runwebscraper.py and requirements.txt file, put them in a folder, and get in that directory.

Before running the .py file, type "pip install -r requirements.txt" to download the required packages for scraping.

The .py file scrapes the Portland weather forecast from forecast.weather.gov and gets the high and low temperatures, time period, short description, and long description.

To run the file, type "runwebscraper.py 5 1000". The  '5' and '1000' can be any numbers, but they are required. The '5' is the amount of seconds in between each scrape. The minimum interval is 2 seconds. The '1000' is the number of cycles the scraping loop goes through. To end the program, either wait until the loop reaches the the required cycles to break, or press ctrl + c in the CLI.

NOTE: if typing "runwebscraper.py" doesn't work, type "python runwebscraper.py".

To skip any of the 4 parameters, type after runwebscraper.py:

  --skipperiod (skip time period)
  
  --skiptemp (skip temperatures)
  
  --skipdesc (skip long description)
  
  --skipshort_desc (skip short description)
  
  i.e "runwebscraper.py --skipdesc 60 300"

The program prints any changes it detects. It also arranges all the data in a pandas table (pandas.DataFrame).
