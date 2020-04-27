#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 23:10:53 2020

@author: alfiantjandra
"""

import requests 

from bs4 import BeautifulSoup 

#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
#soup = BeautifulSoup(page.content,"html.parser")
##print(soup.prettify())
##list(soup.title)
##list(soup.children)
##print(soup.title.parent.name)
##print(soup.p)
#
#html = list(soup.children)[2]
#body = list(html.children)[3]
#p = list(body.children)[1]
#print(p.get_text())
#
#
##soup.find_all('p')
##soup.find_all('head')

#Getting Weather,(pretty cool)
#page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
#soup = BeautifulSoup(page.content, 'html.parser')
#seven_day = soup.find(id="seven-day-forecast")
#forecast_items = seven_day.find_all(class_="tombstone-container")
#tonight = forecast_items[0]
#print(tonight.prettify())
#period = tonight.find(class_="period-name").get_text()
#short_desc = tonight.find(class_="short-desc").get_text()
#temp = tonight.find(class_="temp").get_text()
#print(period)
#print(short_desc)
#print(temp)
total_words = 0
page = requests.get('https://www.apple.com/apple-watch-series-5/')
soup = BeautifulSoup(page.content, 'html.parser')
main = soup.find(id="main")
classes = ['typography-headline-super headline-text bold','icon-copy','typography-headline bold','typography-tout']
#sections = main.find_all(class_='typography-headline-super headline-text bold')
#for section in sections:
#    print(section.get_text().split())

for clasD in classes:
    sections = main.find_all(class_=clasD)
    for section in sections:
        lmao = section.get_text().split()
        total_words += len(lmao)
#        print(lmao)
#        print(len(lmao))

print(total_words)
        