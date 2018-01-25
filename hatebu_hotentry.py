import datetime
import requests
import csv

from bs4 import BeautifulSoup, Tag

target_url = 'http://b.hatena.ne.jp/hotentry'

now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

html = requests.get(target_url)
soup = BeautifulSoup(html.text, "html.parser")
hotentry = soup.find(id="main")

with open('hatebu_hotentry' + now + '.csv', 'w+', encoding="utf-8") as f:
    writer = csv.writer(f, lineterminator='\n')
    html = requests.get(target_url)
    soup = BeautifulSoup(html.text, "html.parser")
    hotentry = soup.find(id="main")
    writer.writerow([now])
    for entry in hotentry.find_all('a', class_="entry-link"):
        writer.writerow([entry.get("href"), entry.get("title")])
