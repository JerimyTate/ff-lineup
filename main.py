from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import requests


url = "https://s3-us-west-1.amazonaws.com/fftiers/out/text_WR-PPR.txt"

r = requests.get(url)
ranks= []
print(r.text)
split_on_lines = r.text.split("\n")

for line in split_on_lines:
    new_line = line.split(': ')
    if len(new_line)==2:
        tier = {"Tier" : new_line.__getitem__(0)}
        players = [new_line.__getitem__(1).split(", "),]
        ranks.append([tier, {"Players": players}])
    else:
        continue



print("Ranks______")
print(ranks)

for line in ranks:
    new_line = line.split(', ')
    print(new_line)
    tier = {new_line[0]}
    print(tier)
    ranks.append(tier)

gametypes = [
    {
        "ppr": "ppr-",
    },
    {
        ".5ppr": "half-05-5-ppr-"
    },
    {
        "standard": ""
    }
]

positions = ["quarterback", "running-back", "wide-receiver", "tight-end", "flex", "kicker,defense-dst"]

#get lineup and game type

#loop through pages and scrape positions and tiers

#loop through tiers and assign to lineup list first n matches where n = number of people at that position

#print out optimal borischen linup