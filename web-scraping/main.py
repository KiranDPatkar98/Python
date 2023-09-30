import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get('https://news.ycombinator.com/newest').text
# print(response)
soup = BeautifulSoup(response, 'html.parser')
# print(soup.title)

# it will find all the div
# print(soup.find_all('div'))

# To find the first appearance
# print(soup.find('div'))
links = soup.select('.titleline')
votes = soup.select('.score')
# print(votes)


def custom_hacker_news(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        # to find the anchor tag inside the titleline
        anchor_tag = item.find('a')
        # to get the href , if not prsent None will be assigend
        href = anchor_tag.get('href')
        points = votes[idx].getText().replace(' points', '')
        # print(points)
        hn.append({'title': title, 'href': href, "votes": points})
    return hn


pprint.pprint(custom_hacker_news(links, votes))
