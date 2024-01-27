import requests
from bs4 import BeautifulSoup
import time
import pprint

#to access the web url
t1 = time.time()
res = requests.get('https://news.ycombinator.com/news')
t2 = time.time()
print(f"response time {t2-t1}")

# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.body.contents)
print(soup.find('a'))
# print(soup.find_all('a')[0])
# print(soup.find_all('a')) #to get all the links (a text)
# print(soup.title)

# print(soup.find(id='score_39151937'))
# print(soup.select('.score')) # to get class of span as score
# print(soup.select('.rank'))
# print(soup.select('.id')) #observed blank as 'id' is not a class name under span class.
# print(soup.select('#score_39151937'))
links = soup.select('.titleline')
votes = soup.select('.score')
subtext = soup.select('.subtext')
# print(votes)
# print(votes[0])
# print(votes[0].get('id'))
# print(links)
# print(links.__dir__())
def create_custom_web(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        yo = links[idx].find('a')
        href = yo.get('href', None)
        vote = subtext[idx].select('.score')
        # print(vote[0].getText())
        if len(vote):

            points = int(vote[0].getText().replace(' points', ''))
            hn.append({'title': title, 'link': href, 'votes': points})
    return hn

print(create_custom_web(links, subtext))
# print(links[0])
# print(soup.get('href'))
# x = soup.find('a')
# print(x.get('href'))
pprint.pprint(create_custom_web(links, subtext))









