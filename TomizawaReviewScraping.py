# coding: UTF-8
import time
import urllib.request, urllib.error
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import consts 
import csv
import sys
import codecs

#sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
urllist_class = consts.urllist

for j in range(len(urllist_class)):

#url = 'https://tomiz.com/item/00008802'
  url = urllist_class[j]
  print(url)

#selenium open review
  options = Options()
  options.add_argument('--headless')
  options.add_argument('--disable-gpu')
  driver = webdriver.Chrome(executable_path='C:\selenium\chromedriver', options=options)
  driver.get(url)
  driver.find_element_by_class_name('btn_basic02').click()
  print(driver.title.encode('utf-8'))
  print('Moving review Page...')
  time.sleep(5)

  product = driver.title.rstrip('のクチコミ | お菓子作り・パン作りなら製菓材料専門店TOMIZ(富澤商店)通販サイト').encode('utf-8')

#open csv File
  f = open('./reviewData.csv', 'a')
  writer = csv.writer(f, lineterminator='\n')

#read Review from Many review page
  for i in range(4):
    try:
      #get the Scraping URL
      url = driver.current_url

      #return the URL from Selenium to BeautifulSoup
      html = urllib.urlopen(url)
      soup = BeautifulSoup(html, "html.parser")

      #Scraping Process Start
      for tag in soup.find_all("div", class_ = 'review_box01'):
        for review in tag.find_all("p"):
          #initialize reviewer list
          reviewlist = []

          review_const = review.prettify()
          #print review_const.encode('utf-8')
          #review initial text         
          reviewer_initial = review_const.find('</time>') + 9
          #review final text
          reviewer_final = review_const.find('<span') - 2
          #get reviewer name
          reviewername = review_const[reviewer_initial:reviewer_final]
          print(reviewername.encode('utf-8'))
          reviewlist.append(reviewername.encode('utf-8'))

          #reviewScore initial text
          reviewscore_initial = review_const.find('star_') + 5
          #reviewScore final text
          reviewscore_final = reviewscore_initial + 1
          #get reviewScore
          reviewscore = review_const[reviewscore_initial:reviewscore_final]
          print(reviewscore.encode('utf-8'))
          reviewlist.append(reviewscore.encode('utf-8'))

          #get productname
          reviewlist.append(product.encode('utf-8'))
          
          #write csv file
          writer.writerow(reviewlist)

      driver.find_element_by_class_name('next').click()
      print('go to Next Review Page...')
      time.sleep(5)
    except:
      print('Completed! writing csv')
#close csv file
      f.close()
#close selenium
      driver.close()
      driver.quit()
      break

