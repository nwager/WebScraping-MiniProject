# WebScraping-MiniProject
My weatherscraper.py and requirements.txt files.

## Installation

Make sure you have Python 2.7.10 up to 2.7.14 installed.

Install the newest version of ChromeDriver for the correct platform here: https://sites.google.com/a/chromium.org/chromedriver/downloads

(ChromeDriver allows the program to control browsers, like opening windows and going to sites).

Extract the .zip file and put the executable in your Path environmental variable by doing this (Windows):

1. Start the System Control Panel applet (Start - Settings - Control Panel - System).  
2. Select the Advanced tab.  
3. Click the Environment Variables button.  
4. Under System Variables, select Path, then click Edit and put the executable or its folder in PATH.  

Next, install the weatherscraper.py and requirements.txt files, put them in a folder, set up your virtual environment, and get in that directory in the console.  
Before running the .py file, type `pip install -r requirements.txt` into the console to download the required packages for scraping.

You can look at the code here, in GitHub. I left a lot of comments ;).


## Usage
The .py file scrapes the weather forecast from forecast.weather.gov and gets the high and low temperatures, time period, short description, and long description.

To run the file without skipping any parameters, you can type this example into the console:  
`python weatherscraper.py 5 2 minutes 'Portland'`  
<b>NOTE:</b> if this doesn't work, switch between `python weatherscraper.py` and `weatherscraper.py`

The `5` specifies the amount of seconds between each scrape. This can be any number.

The `2 minutes` specifies how long the program runs.  
You can type any number, and after it you have to write `seconds`,       `minutes`, or `hours` to specify the unit of time.

The `'Portland'` specifies the US city. Type in any US city, but have quotes around it.

To end the program, either wait for the time to run out or force it to end by pressing `ctrl + c`.

<b>Optional Parameters</b>  
To skip any of the 4 parameters, type after weatherscraper.py and before the numbers:

`--skipperiod` (skip time period)  
`--skiptemp` (skip temperatures)  
`--skipdesc` (skip long description)  
`--skipshort_desc` (skip short description)

i.e. `weatherscraper.py --skipdesc 60 3 hours 'Los Angeles'`

The program prints any changes it detects. It also arranges all the data into a pandas table (pandas.DataFrame).
