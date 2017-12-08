#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup

url = 'http://store.steampowered.com/app/401920'
url = 'http://store.steampowered.com/app/20'

# cookie to get through age check
cookies = {'birthtime': '568022401'}
filterString = '.responsive_apppage_details_left.game_details .details_block'



# get the html data and parse it
html_response = requests.get(url, cookies=cookies).text
soup = BeautifulSoup(html_response, 'html.parser')

# get game details, it's in the first block
game_details = soup.select(filterString)[0].prettify()
game_details = game_details.replace('\n', '')
game_details = game_details.split('<br/>')

# parse string
title = game_details[0].split('</b>')[1]
genre = game_details[1].split('</b>')[1].split("\">")[1].replace('</a>','')
developer = game_details[2].split('</b>')[1].split("\">")[1].replace('</a>','')
publisher = game_details[3].split('</b>')[1].split("\">")[1].replace('</a>','')
release_date = game_details[4].split('</b>')[1]

print(title,genre, developer, publisher, release_date)
# print(developer)
# print(publisher)
# print(release_date)
# title
