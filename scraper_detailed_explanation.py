# import the required libraries
# requests is used to request for webssite resources from the server that hosts it
import requests
# BeautifulSoup is used to parse (read for us the html code and extract out only the parts we want)
from bs4 import BeautifulSoup


# this is the url of the page we are scraping from
# it is a google search page for searching "python kampala uganda"
url = "https://www.google.com/search?&q=python+kampala+uganda"

# make a get request to fetch the websites resources from the server using requests.get(url)
response = requests.get(url) 
'''
store it in a response object because when we make a 'request', we are asking for a 'response'
it is like you ask a question(request), and get and answer (response)
'''

# this extracts the html code part from our response object
html = response.text

# now, we parse the html using BeautifulSoup
soup = BeautifulSoup(html, "lxml")
'''
we store the parsed html in a variable called soup
we use a library called html.parse, don't worry about this. More on that later :-)
'''


'''
next; we shall be using; find (when looking for one element from the html) or find_all (when looking for many elements from the html)
remember to right click an element that you are intereted in on its website using chrome, 
choose 'inspect element' to see the element's html tag
'''


# Now, lets scrape the websites title
title = soup.find("title").text
'''
we use find ( because we are looking for one element from the html )
the title is in the <title> tag when you inspect chrome
we use dot notation to get its text ('.text')
we have stored the title in a varibale called title
'''
print(" -- RESULT WEBSITE TITLE --")
print(title)




print
# lets print out all headers of search results
results_headings = soup.find_all("h3")
'''
the search reslts are in <h3> tags when you inspect the website element in chrome
'''
print(" -- SEARCH RESULT HEADINGS --")
# iterrate over the resulsts (using a for loop) and print out the headers one by one
for results_heading in results_headings:
	# print the link text
	print(results_heading.text)





print
# lets print out all url links of search results
results_links = soup.find_all("cite")
'''
the search results are in <cite> tags when you inspect the website element in chrome
'''
# iterrate over the resulsts (using a for loop) and print out the links one by one
print(" -- SEARCH RESULT LINKS --")
for results_link in results_links:
	# print the link text
	print(results_link.text)





