import requests
from bs4 import BeautifulSoup
import time

#to access the web url
t1 = time.time()
res = requests.get('https://news.ycombinator.com/news')
t2 = time.time()
print(f"response time {t2-t1}")

# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)
print(soup.find('a'))
# print(soup.find_all('a')) #to get all the links (a text)
# print(soup.title)





