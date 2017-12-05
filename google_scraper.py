# import the required libraries
import requests
from bs4 import BeautifulSoup


# this is the url of the page we are scraping from, copied from browser
url = "https://www.google.com/search?&q=python+kampala+uganda"
# make a get request to fetch the websites resources from the server using requests.get(url)
response = requests.get(url) 
# this extracts the html code part from our response object
html = response.text
# now, we parse the html using BeautifulSoup
soup = BeautifulSoup(html, "lxml")


# Now, lets scrape the websites title
title = soup.find("title").text
print(" -- RESULT WEBSITE TITLE --")
print(title)


print
# lets print out all headers of search results
results_headings = soup.find_all("h3")
print(" -- SEARCH RESULT HEADINGS --")
for results_heading in results_headings:
	print(results_heading.text)


print
# lets print out all url links of search results
results_links = soup.find_all("cite")
print(" -- SEARCH RESULT LINKS --")
for results_link in results_links:
	print(results_link.text)


