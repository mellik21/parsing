import requests
from bs4 import BeautifulSoup

from twitter_scrapy.twitter.items import Tweet

URL = 'https://twitter.com/Krua_nyan/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}
HOST = 'https://twitter.com'


def get_html(url, params=None):
    r = requests.get(url, stream=True)
    with r as response:
        size = sum(len(chunk)
                   for chunk in response.iter_content(8196))
    print(size)

    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('a', class_='css-1dbjc4n r-1iusvr4 r-16y2uox r-1777fci r-1mi0q7o')

    tweets = []
    for item in items:
        tweet = Tweet()
        tweet['text'] = item.find('div',
                                  class_='css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim '
                                         'r-qvutc0').get_text()
        tweet['date'] = item.find('time').get_text()
        tweet['author'] = item.find('div', class_='css-1dbjc4n r-1wbh5a2 r-dnmrzs').get_text()
        tweet['likes'] = item.find('span',
                                   class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0').get_text()

        tweets.append(tweet)
        print(tweet)
    return tweets


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        tweets = get_content(html.text)
    else:
        print('Error')


parse()
