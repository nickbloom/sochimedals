## Scrapeit - A Simple Tumblr Scraper
## version 0.1 - Last Updated 2/18/13
## created by Nick Bloom
## CC NonCommercial-ShareAlike 
## If you do something cool with it, or make improvements, please let me know
## datetime.date(2010, 6, 13)
## datetime.date(2010, 5, 14)

from bs4 import BeautifulSoup
import urllib.request
import os
import numpy
import re


manmedals = []
womedals = []
url="http://www.sochi2014.com/en/medal-winners?country=all&sport=all&gender=men&gold=yes&silver=yes&bronze=yes"
urlw="http://www.sochi2014.com/en/medal-winners?country=all&sport=all&gender=women&gold=yes&silver=yes&bronze=yes"

rule1=re.compile(r'(?<=\– )[A-Za-z\s]{1,20}(?= Lyrics)')

title="medals"

newdir = "/Users/nbloom/Transporter/nick/scripts/sochi/" + title
if not os.path.exists(newdir):
	os.makedirs(newdir)


request = urllib.request.Request(url)
request.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
html = urllib.request.urlopen(request).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)
usas = soup.find_all("td", attrs={'class': re.compile(r"usa")})

for usa in usas:
	medalset = usa.find_next("ul", attrs={'class': re.compile(r"medalset")})
	medal = medalset.li
	medal = medal['class']
	medal = ''.join(medal)
	manmedals.append(medal)

gold = manmedals.count('gold')
silver = manmedals.count('silver')
bronze = manmedals.count('bronze')

filename = str(newdir) + "/" + "men" + ".csv"
file = open(filename,"w")
file.write("Gold,Silver,Bronze\n" + str(gold) + "," + str(silver) + "," + str(bronze) + "\n")
file.close()

request = urllib.request.Request(urlw)
request.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
html = urllib.request.urlopen(request).read()
h = html.decode('utf-8')
soup = BeautifulSoup(h)
usas = soup.find_all("td", attrs={'class': re.compile(r"usa")})

for usa in usas:
	medalset = usa.find_next("ul", attrs={'class': re.compile(r"medalset")})
	medal = medalset.li
	medal = medal['class']
	medal = ''.join(medal)
	womedals.append(medal)

gold = womedals.count('gold')
silver = womedals.count('silver')
bronze = womedals.count('bronze')

filename = str(newdir) + "/" + "women" + ".csv"
file = open(filename,"w")
file.write("Gold,Silver,Bronze\n" + str(gold) + "," + str(silver) + "," + str(bronze) + "\n")
file.close()
