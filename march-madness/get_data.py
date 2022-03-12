import requests
from bs4 import BeautifulSoup
from os import path
import pdb

year = 2019
URL = f"https://barttorvik.com/trank.php?year={year}&sort=&top=0&conlimit=All#"
file_name = f"data-{year}.html"
content = None
if path.exists(file_name):
    with open(file_name, "r") as f:
        content = f.read()
else:
    page = requests.get(URL)
    content = page.text
    with open(file_name, "w") as f:
        f.write(content)

soup = BeautifulSoup(content, "html.parser")

table = soup.table
pdb.set_trace()
rows = table.find_all("tr")

output = []

for row in rows[2:]:
    cols = row.find_all("td")
    print(cols)

    row_output = {}
    cell_one = list(cols[1].strings)
    row_output["name"] = cell_one[]
    
