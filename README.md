# Steam data scraper

Short script to scrape game details (title, developer, publisher, release date and genre) from Steam.

**Region locked games** cannot be fetched from steam. For example the Dishonored RHCP (Russian, Hungarian, Czech, Polish) version's id is 217980, but in another region is 205100. Because of this, I'll use the [SteamDB](https://steamdb.info) website

## How to run the script
```bash
python3 run.py -i data.json -o output.csv   
```

### Parameters

The script has two mandatory parameters:
- `i` is the input file
- `o` output file name. Mandatory and has to be a string.

### Input file
Use the **json** from [http://store.steampowered.com/dynamicstore/userdata/](http://store.steampowered.com/dynamicstore/userdata/) website after you logged in on [web Steam](store.steampowered.com). The script only uses the `rgOwnedApps` array.

```json
{
   "rgOwnedApps":[8340]
}
```



### Output file
The output file will be a csv file.
```
"title","developer","publisher","release_date","genre"
" Team Fortress Classic ","  Valve  ","  Valve  "," 1 Apr, 1999 ","  Action  "
" Half-Life: Opposing Force ","  Gearbox Software  ","  Valve  "," 1 Nov, 1999 ","  Action  "
" Half-Life ","  Valve  ","  Valve  "," 8 Nov, 1998 ","  Action  "
```

### Example log output
The script does a simple `print()` output to let you know which games were successfully scraped and which ones were not.
```
Scraping game data with id 254440.
Scraping game data with id 255300.
The game with id 255520 doesn't exist anymore.
Scraping game data with id 255980.
Scraping game data with id 257070.
```

## Dependency
HTML parser:  [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).
