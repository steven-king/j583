#!/usr/bin/env python

import urllib2
from bs4 import BeautifulSoup

url = 'http://steventking.com/resume.html' # write the url here
output =""
usock = urllib2.urlopen(url)
html_data = usock.read()
usock.close()
print "Socket Opened, html_data stored and scoket closed"
#print html_data

soup = BeautifulSoup(html_data)

#print "Make it pretty"
#print soup

tempData = soup.find_all('h1')
for names in tempData:
    output += names.string

output += " has worked for "


tempData = soup.find_all('h4')
for companies in tempData:
    
    output += companies.string + ','

print output





