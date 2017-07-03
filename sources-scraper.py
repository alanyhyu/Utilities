from bs4 import BeautifulSoup
import urllib
import codecs
import webbrowser


soup = BeautifulSoup(urllib.request.urlopen('https://sources.npr.org/science/'),'lxml')
#print (soup.prettify())
print (soup.get_text())

div_content = soup.find_all("div", class_="entry-content")
print (div_content)

##for link in soup.find_all("a"):
##    print(link.get('href'))





import csv
from bs4 import BeautifulSoup
import urllib
import webbrowser
import re

links =[]

with open('ScienceSources.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        joined = ''.join(row)
        links.append(joined)

for link in links:
    soup2 = BeautifulSoup(urllib.request.urlopen(link), "lxml")
    name = soup2.find_all("h1", class_="entry-title")
    print(name)
    f = urllib.request.urlopen(link)
    s = f.read().decode('utf-8')
    print(re.findall(r"\+\d{2}\s?0?\d{10}",s))
##    contact_info = soup2.find_all("blockquote")
##    print(contact_info)




## get list of URLs to individual sources
## open all URLs
## scrape the name, first row of entry content/bio, and contact information in three separate lists
