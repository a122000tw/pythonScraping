from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("https://mofanpy.com/static/scraping/basic-structure.html"
               ).read().decode('utf-8')
print(html)

soup = BeautifulSoup(html, features="lxml")
print(soup.h1)
print('\n', soup.p)
all_href = soup.find_all('a')
for l in all_href:
    print("href = ", l['href'])