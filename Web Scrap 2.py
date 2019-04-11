# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 10:08:02 2019

@author: Sameer
"""

import bs4
import requests
import urllib


url = 'https://www.indeed.co.in/jobs?q=python&start=0'
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text,'html.parser')


# Finding Total jobs
result = soup.findAll('div',{'id':'searchCount'})
for r in result:
    total_jobs=r.text
total_jobs=total_jobs.split(' ')
total_jobs=int(total_jobs[-2].replace(',',''))

# Title
job_title=[]
result = soup.findAll('a',{'data-tn-element':'jobTitle'})
for r in result:
    job_title.append(r.get('title'))
#
## Company
#company = []
#result = soup.findAll('span',{'class':'company'})
#for r in result:
#    name= r.text
#    name=name.lstrip()
#    name=name.rstrip()
#    company.append(name)
#
## Location 
#result = soup.findAll('div',{'class':'location'})
#result1 = soup.findAll('span',{'class':'location'})
#    
title=[]
company=[]
location=[]
summary=[]
result = soup.findAll('div',{'class':'jobsearch-SerpJobCard'})
for r in result:
    t=r.find('a',{'data-tn-element':'jobTitle'}).text
    t=t.lstrip()
    t=t.rstrip()
    title.append(t)
    c = r.find('span',{'class':'company'}).text
    c=c.lstrip()
    c=c.rstrip()
    company.append(c)
    l=r.find('',{'class':'location'}).text
    l=l.lstrip()
    l=l.rstrip()
    location.append(l)
    s=r.find('',{'class':'summary'}).text
    s=s.lstrip()
    s=s.rstrip()
    summary.append(s)
    


total_page=round(total_jobs/len(job_title))
i=10
while i < 1000:
    link='https://www.indeed.co.in/jobs?q=python&start='+str(i)
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text,'html.parser')
    result = soup.findAll('div',{'class':'jobsearch-SerpJobCard'})
    for r in result:
        t=r.find('a',{'data-tn-element':'jobTitle'}).text
        t=t.lstrip()
        t=t.rstrip()
        title.append(t)
        c = r.find('span',{'class':'company'}).text
        c=c.lstrip()
        c=c.rstrip()
        company.append(c)
        l=r.find('',{'class':'location'}).text
        l=l.lstrip()
        l=l.rstrip()
        location.append(l)
        s=r.find('',{'class':'summary'}).text
        s=s.lstrip()
        s=s.rstrip()
        summary.append(s)
    i=i+10