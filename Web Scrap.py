# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 14:55:07 2019

@author: Sameer
"""

#1. Extract all the image links and then the images from
#'https://en.wikipedia.org/wiki/Mahatma_Gandhi'. Extract
#the image only if ‘Gandhi’ appears in the url.
import bs4
import requests
import urllib
import re

url = 'https://en.wikipedia.org/wiki/Mahatma_Gandhi'
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')
image_links=[]
# Extracting href links from img tag
tag = soup('img')
for link in tag:
    if link.get('src') != None:
       image_links.append(link.get('src'))     

# Extracting links which has Gandhi
gandhi_links=[]
for r in image_links:
    if r.find('gandhi')>-1 or r.find('Gandhi')>-1:
        gandhi_links.append(r)

import uuid
#unique_filename = str(uuid.uuid4())
    
for url in gandhi_links:
    unique_filename = str(uuid.uuid4())
    fimg = open('C:\Sameer\Data Science\Aegis\Python\Web Scraping\images\gandhi'+unique_filename,'wb')
    url="https:"+url
    data = urllib.request.urlopen(url)
    buffersize = 100000
    info = data.read(buffersize)
    while len(info):
        fimg.write(info)
        info=data.read(buffersize)
    fimg.close()


#2Extract all language names and number of articles from
#‘https://www.wikipedia.org/'.

url = 'https://www.wikipedia.org/'
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')
result = soup.findAll('a',{'class':'link-box'})
article = soup.findAll('bdi',{'':'ltr'})
lang =dict()
for r in result:
    lang[r.find('strong').text]=r.find('bdi').text

#3 3. List Top bollywood movies with their
#number(position),name, year, genre and rating from
#'https://www.imdb.com/list/ls021116007/'. Create a SQL
#table and insert these values in it.
    
url = 'https://www.imdb.com/list/ls021116007/'
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')
films = soup.findAll('h3',{'class':'lister-item-header'})
result = soup.findAll('div',{'class':'lister-item mode-detail'})   
rank=[]
film=[]
year=[]
rating=[]

for r in result:
    rank.append(r.find('span',{'class':'lister-item-index unbold text-primary'}).text)
    year.append(r.find('span',{'class':'lister-item-year text-muted unbold'}).text)
    rating.append(r.find('span',{'class':'ipl-rating-star__rating'}).text)

for f in films:
    film.append(f.find('a').text)

film[1]
import sqlite3
con = sqlite3.connect('movies.db')
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS MOVIES')
cur.execute('CREATE TABLE MOVIES (RANK INT, FILM VARCHAR(50), YEAR VARCHAR(20), RATING VARCHAR(10))')
for i in range(len(rank)):
    cur.execute('INSERT INTO MOVIES VALUES(?,?,?,?)',(rank[i],film[i],year[i],rating[i]))

con.commit()
cur.execute('SELECT * FROM MOVIES')
for rows in cur:
    print(rows)
    