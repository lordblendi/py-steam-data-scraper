#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup
import csv
import io

url_prefix = 'http://store.steampowered.com/app/'
filter_string = '.responsive_apppage_details_left.game_details .details_block'
# cookie to get through age check
cookies = {'birthtime': '568022401'}





# create csv file and add columns
csvfile = open("output.csv", "w", newline="")
writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
writer.writerow(['title', 'developer', 'publisher', 'release_date', 'genre'])


url = url_prefix + "130"
# get the html data and parse it
html_response = requests.get(url, cookies=cookies).text
soup = BeautifulSoup(html_response, 'html.parser')
# get game details, it's in the first block
game_details = soup.select(filter_string)[0].prettify()


game_details = game_details.replace('\n', '')
game_details = game_details.split('<br/>')
# parse string parts
title = game_details[0].split('</b>')[1]
genre = game_details[1].split('</b>')[1].split("\">")[1].replace('</a>','')
developer = game_details[2].split('</b>')[1].split("\">")[1].replace('</a>','')
publisher = game_details[3].split('</b>')[1].split("\">")[1].replace('</a>','')
release_date = game_details[4].split('</b>')[1]

writer.writerow([title, developer, publisher, release_date, genre])
