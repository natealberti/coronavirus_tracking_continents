# coronavirus_tracking_continents
Scrapes live coronavirus data from Worldometers with BeautifulSoup

This program retrieves live daily data from https://www.worldometers.info/coronavirus/ with beautifulsoup and puts it into a nice readable
table using pandas. Inside the region.py file, that's where I sorted through the source code of the website to grab the stats, and then set
up some nice accessor functions for the 'region' object. In the test_class.py file I grouped the relavent data together in series and joined
them in one big dataframe.
I'm planning on doing something similar with US states so I have more rows to draw from. 
