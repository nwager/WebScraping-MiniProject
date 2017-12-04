# WebScraping-MiniProject
My weatherscraper.py and requirements.txt files.

## Installation

Make sure you have Python 2.7.10 up to 2.7.14 installed.

Install the newest version of ChromeDriver for the correct platform here: https://sites.google.com/a/chromium.org/chromedriver/downloads

(ChromeDriver allows the program to control browsers, like opening windows and going to sites).

Extract the .zip file and put this folder:

![ChromeDriver Folder](/images/cdriverfolder.PNG)

in your Path environmental variable by doing this (Windows):

1. Start the System Control Panel applet (Search "System" and click - it should be the Control Panel).  
2. Select the Advanced system settings tab.  
3. Click the Environment Variables button.  
4. Under System Variables, select Path, click Edit, then click Browse.
5. Find the folder (it's probably in Downloads) and put it in the Path.

Here's a slightly fast gif of that:

![How to edit Path](/images/chromedriverpath.gif)

Next, install the weatherscraper.py and requirements.txt files, set up your virtual environment, and get in the directory containing the scripts in the console.  
Before running the .py file, type `pip install -r requirements.txt` into the console to download the required packages for scraping.

You can look at the code here, in GitHub. I left a lot of comments ;).


## Usage
The .py file scrapes the weather forecast from forecast.weather.gov and gets the high and low temperatures, time period, short description, and long description. The program prints any changes it detects. It also arranges all the data into a pandas table (pandas.DataFrame).

To run the file without skipping any parameters, you can type this example into the console:  
`python weatherscraper.py 2 4 seconds 'Portland'`  

It should look something like this:

![Weather Scraping Example](/images/skipdesc.PNG)

The `2` specifies the amount of seconds between each scrape. This can be any number.

The `4 seconds` specifies how long the program runs.  
You can type any number, and after it you have to write `seconds`, `minutes`, or `hours` to specify the unit of time.

The `'Portland'` specifies the US city. Type in any US city, but have quotes around it.

To end the program, either wait for the time to run out or force it to end by pressing `ctrl + c`.  
**NOTE:** If a window pops up saying "chromedriver.exe has stopped working" or something, that's fine; just click OK.

<b>Optional Parameters</b>  
To skip any of the 4 parameters, type after weatherscraper.py and before the numbers:

`--skipperiod` (skip time period)  
`--skiptemp` (skip temperatures)  
`--skipdesc` (skip long description)  
`--skipshort_desc` (skip short description)

i.e. `python weatherscraper.py --skipdesc 2 4 seconds 'Portland'`

The example should look like this:

![Weather Scraping Example - skipdesc](/images/webscraperpic.PNG)

If you got everything to work, then yay! You're done!

Here's a flowchart I made using draw.io:

![weatherscraper.py flowchart](/images/WeatherScraperDiagram.PNG)
