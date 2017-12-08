#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup
import csv
import io
import argparse
import json

# settings arguments
parser = argparse.ArgumentParser(
    prog='run.py', description="Script to scrape game details from steam and write it into a csv file")
parser.add_argument('-i', metavar='input',
                    help="input filename", required=True, type=str)
parser.add_argument('-o', metavar='output',
                    help="output filename", required=True, type=str)
args = parser.parse_args()


url_prefix_steam = 'http://store.steampowered.com/app/'
url_prefix_steamdb = 'https://steamdb.info/app/'
filter_string_steam = '.responsive_apppage_details_left.game_details .details_block'
filter_string_steamdb = '.row.app-row tbody tr'
# cookie to get through age check
cookies = {'birthtime': '568022401'}
columns = ['title', 'developer', 'publisher', 'release_date', 'genre']

# parsing json

json_file = open(args.i).read()
json_data = json.loads(json_file)
rgOwnedApps = json_data['rgOwnedApps']

with open(args.o, "w", newline="") as csvfile:
    # create csv file and add columns
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(columns)

    for game_id in rgOwnedApps:
        url = url_prefix_steam + str(game_id)

        # get the html data and parse it
        html_response = requests.get(url, cookies=cookies)
        soup = BeautifulSoup(html_response.text, 'html.parser')
        soup_data = soup.select(filter_string_steam)

        # to make sure the game still exists
        if len(soup_data) > 0:
            print("Scraping game data with id {0}.".format(game_id))
            # get game details, it's in the first block
            soup_prettified = soup_data[0].prettify()

            # parse string parts
            game_details = soup_prettified.replace('\n', '').split('<br/>')
            title = ""
            developer = ""
            genre = ""
            publisher = ""
            release_date = ""
            # make sure the items exists
            for detail in game_details:
                if "Title" in detail:
                    title = detail.split('</b>')[1]

                if "Genre" in detail:
                    splitted_links = detail.split('</b>')[1].split(", <a")
                    data_array = []
                    for link in splitted_links:
                        data_array.append(link.split(
                            "\">")[1].replace('</a>', ''))
                    genre = ','.join(data_array)

                if "Developer" in detail:
                    splitted_links = detail.split('</b>')[1].split(", <a")
                    data_array = []
                    for link in splitted_links:
                        data_array.append(link.split(
                            "\">")[1].replace('</a>', ''))
                    developer = ','.join(data_array)

                if "Publisher" in detail:
                    splitted_links = detail.split('</b>')[1].split(", <a")
                    data_array = []
                    for link in splitted_links:
                        data_array.append(link.split(
                            "\">")[1].replace('</a>', ''))
                    publisher = ','.join(data_array)

                if "Release" in detail:
                    release_date = detail.split('</b>')[1]

            # write details into the csv file
            writer.writerow([title, developer, publisher, release_date, genre])
        else:
            print("The game with id {0} doesn't exist in your Steam region. Trying to fetch it from SteamDB.".format(
                game_id))

            url = url_prefix_steamdb + str(game_id)

            html_response = requests.get(url)
            soup = BeautifulSoup(html_response.text, 'html.parser')
            soup_data_rows = soup.select(filter_string_steamdb)

            title = ""
            developer = ""
            genre = ""
            publisher = ""
            release_date = ""

            for row in soup_data_rows:
                cells = row.select('td')
                name = str(cells[0])
                data = str(cells[1])
                if "alternateName" in data:
                    title = data.split("\">")[1].replace('</td>', '')
                if "author" in data:
                    developer += data.split("\">")[1].split('<')[0]
                if "publisher" in data:
                    publisher += data.split("\">")[1].split('<')[0]
                if "Release Date" in name:
                    release_date = data.replace('<td>', '').split('<')[0]

            writer.writerow([title, developer, publisher, release_date, genre])
