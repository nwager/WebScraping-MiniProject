# WebScraping-MiniProject
My weatherscraper.py and requirements.txt files. These files are meant for a CLI.

First, install ChromeDriver for the correct platform here: https://sites.google.com/a/chromium.org/chromedriver/downloads

Extract the .zip file and put the executable in PATH. For Windows:

1. Start the System Control Panel applet (Start - Settings - Control Panel - System).  
2. Select the Advanced tab.  
3. Click the Environment Variables button.  
4. Under System Variables, select Path, then click Edit and put the executable or its folder in PATH.  

Next, nstall the weatherscraper.py and requirements.txt files, put them in a folder, and get in that directory in the CLI.  
Before running the .py file, type "pip install -r requirements.txt" to download the required packages for scraping.

The .py file scrapes the weather forecast from forecast.weather.gov and gets the high and low temperatures, time period, short description, and long description.

To run the file without skipping any parameters, type: 

  weatherscraper.py 5 2 minutes 'Portland'.  
  <b>NOTE:</b> if typing "weatherscraper.py" doesn't work, type "python weatherscraper.py".
  
  The "5" specifies the amount of seconds between each scrape.
  
  The "2 minutes" specifies how long the program runs. You can type any number, and after it you have to write "seconds",       "minutes", or "hours" to specify the unit of time.
  
  The "'Portland'" specifies the US city. Type in any city, but have quotes around it.
  
To end the program, either wait for the time to run out or force it to end by pressing ctrl + c.

To skip any of the 4 parameters, type after weatherscraper.py and before the numbers:

  --skipperiod (skip time period)
  
  --skiptemp (skip temperatures)
  
  --skipdesc (skip long description)
  
  --skipshort_desc (skip short description)
  
  i.e. "weaherscraper.py --skipdesc 60 3 hours 'Los Angeles'"

The program prints any changes it detects. It also arranges all the data in a pandas table (pandas.DataFrame).
