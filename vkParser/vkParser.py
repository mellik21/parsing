import csv
import time

import requests


def take_1000_posts():
    token = '26c0091426c0091426c00914da26b414a1226c026c0091479af2a50c5ffd63a3cdfb5cb'
    version = 5.124
    domain = 'samara_it_community'
    # krua_official
    offset = 0
    count = 100
    all_posts = []

    while (offset < 1000):
        print('try to parse', offset)
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                })

        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts


def file_writer(all_posts):
    with open('posts.csv', 'w') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('id', 'date', 'views', 'likes', 'reposts', 'body','comments'))
        print(all_posts[0])
        for post in all_posts:
            a_pen.writerow(
                (post['id'], post['date'], post['views']['count'], post['likes']['count'], post['reposts']['count'],
                 post['text'], post['comments']['count']))


all_posts = take_1000_posts()
file_writer(all_posts)
