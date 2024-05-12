import requests
from bs4 import BeautifulSoup

# Import required modules
from lxml import html
import requests

# Request the page
page = requests.get('https://www.twitter-trending.com/turkey/tr')

# Parsing the page
# (We need to use page.content rather than 
# page.text because html.fromstring implicitly
# expects bytes as input.)
tree = html.fromstring(page.content) 

# Get element using XPath
buyers = tree.xpath('//*[@id="gun_one_c"]/div/div[1]/span[2]/a')
print(buyers)

"""
# Downloading contents of the web page
url = "https://getdaytrends.com/united-states"
data = requests.get(url).text


# Creating BeautifulSoup object
soup = BeautifulSoup(data, 'html.parser')


print('Classes of each table:')
for table in soup.find_all('div'):
    print(table.get('class'))
"""