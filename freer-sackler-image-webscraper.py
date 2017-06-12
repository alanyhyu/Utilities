from bs4 import BeautifulSoup
import urllib
import urllib2
import codecs
import webbrowser

## this scrapes all the pages with numbered sequences in the urls

links = []
download_list = []
image_names = []

## this  generates all the urls

for i in range (1,11):
    links.append("http://www.asia.si.edu/collections/edan/default.cfm?searchTerm=avalokitesvara%20or%20kannon&start={}&page={}".format(16*i,i))

## this generates the list of urls for high resolutions images and the list of alt-text that we can use for filenames 
    
for link in links:
    print link
    soup = BeautifulSoup(urllib2.urlopen(link), "lxml")
##    print (soup.prettify())
    div_inside = soup.find_all("div", class_="valign_inside")
    for line in div_inside:
        for element in line:
            print element
            img = element.find('img')['src']
            download_link = img.replace("&max=150","")
            print download_link
            download_list.append(download_link)
            alt = element.find('img')['alt']
            image_names.append(alt)
            
print download_list
print image_names

## this adds a count because sometimes two images have the same alt-text

count = 0

for image in image_names:
    image_filenames.append(image + '%d.jpg' % count)
    count += 1

print image_filenames

for url, name in zip(download_list,image_filenames):
    print (url,name)
    urllib.urlretrieve(url,name)
    
## this scrapes the first page, which doesn't have a numbered sequence in the url

download_list_1 = []
image_names_1 = []
image_filenames_1 = []


first_page_soup = BeautifulSoup(urllib2.urlopen('http://www.asia.si.edu/collections/edan/default.cfm?searchTerm=avalokitesvara%20or%20kannon#accession'), "lxml")
##    print (soup.prettify())
div_inside_1 = first_page_soup.find_all("div", class_="valign_inside")
for line in div_inside_1:
    for element in line:
        print element
        img = element.find('img')['src']
        download_link = img.replace("&max=150","")
        print download_link
        download_list_1.append(download_link)
        alt = element.find('img')['alt']
        image_names_1.append(alt)
        
print download_list_1
print image_names_1

count = 0

for image in image_names_1:
    image_filenames_1.append(image + '%d.jpg' % count)
    count += 1

for url, name in zip(download_list_1,image_filenames_1):
    print (url,name)
    urllib.urlretrieve(url,name)

