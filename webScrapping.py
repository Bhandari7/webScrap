import requests
from bs4 import BeautifulSoup
import time

#to access the web url
res = requests.get('https://news.ycombinator.com/news')
t1 = time.time()
print(res.text)
t2 = time.time()
print(f"response time {t2-t1}")




