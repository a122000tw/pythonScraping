from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://zh.wikipedia.org"
his = ["/wiki/%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2"]
for i in range(20):
    url = base_url + his[-1]
    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    print(soup.find('h1').get_text(), 'url:', his[-1])

    sub_urls = soup.find_all("a", {"href": re.compile('/wiki/(%.{2})+$')})
    # print(sub_urls)
    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()



