# Steam data scraper

Short script to scrape game details (title, developer, publisher, release date and genre) from steam.

## How to run the script
```bash
python3 run.py -i data.json -o output.csv   
```

### Parameters

The script has two mandatory parameters:
- `i` is the input file
- `o` output file name. Mandatory and has to be a string.

### Input file
Input data: Use the **json** from [http://store.steampowered.com/dynamicstore/userdata/](http://store.steampowered.com/dynamicstore/userdata/) website after you logged in on web steam. The script only uses the `rgOwnedApps` array.

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

## Dependency
HTML parser:  [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup).
