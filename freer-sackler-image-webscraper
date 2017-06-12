from bs4 import BeautifulSoup
import urllib
import urllib2
import codecs
import webbrowser

links = []
download_list = []
image_names = []

for i in range (1,11):
    links.append("http://www.asia.si.edu/collections/edan/default.cfm?searchTerm=avalokitesvara%20or%20kannon&start={}&page={}".format(16*i,i))

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

image_filenames = [image + '.jpg' for image in image_names]
print image_filenames

for url, name in zip(download_list,image_filenames):
    print (url,name)
    urllib.urlretrieve(url,name)
