# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

c = csv.writer(open("linkedin-group-results.csv", "wb"))
c.writerow(["Member","Profile"])
driver = webdriver.Chrome(executable_path=r'/Users/dom/Desktop/dev/chromedriver') # YOU WILL NEED TO CHANGE THIS FILE PATH


your_groups_code = """

Enter-Group-Source-Code-Here

"""

users = []
ul = []
def search_bing(name):
    n = name.replace(" ", "+")
    driver.get("https://duckduckgo.com/?q=linkedin+" + n + "&t=hb&ia=web")
    time.sleep(3)
    s = BeautifulSoup(driver.page_source, 'lxml')
    fr = s.find("div", class_="result__body links_main links_deep")

    for a in fr.find_all('a'):
        try:
            if 'linkedin.com/in' in a['href']:
                print 'found linkedin url', a['href']
                if a['href'] in ul:
                    print 'skipping dup'
                else:
                    ul.append(a['href'])
                    c.writerow([name, a['href']])
                    break
        except Exception as e:
            print e,'..continue'


soup = BeautifulSoup(your_groups_code, 'lxml')
for a in soup.find_all('img'):
    name = a['alt']
    if name in users:
        print 'skipping dup'
    else:
        users.append(name)

if len(users) > 1:
    print 'LIST -->', users
    for i in users:
        print "Scraping", i
        search_bing(i)
else:
    print 'Congrats! Your making progress.. Now please insert the code of the linkedin group you want to scrape (as seen in tutorial)'
