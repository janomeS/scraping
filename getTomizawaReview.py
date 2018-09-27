# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

#Target URL
url = "https://tomiz.com/item/00316702?page=4"

#Access URL return HTML
html = urllib2.urlopen(url)

#Control HTML to BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

review = ''

#get Tomizawa revue box
#for tag in soup.find_all("div", class_ ='review_box01'):
 # for review in tag.find_all("p"):
  #  print review.prettify().encode('utf-8')


for tag2 in soup.find_all("h1", class_ = 'h1_basic01'):
  print tag2.prettify().encode('utf-8')


print soup.find("h1", class_='h1_basic01').encode('utf-8')
