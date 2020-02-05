import requests
from bs4 import BeautifulSoup


page = requests.get("https://theinternship.io")
html = page.content
soupPlate = BeautifulSoup(html, features="html.parser")

logo = soupPlate.find_all("img", "center-logos")    # Find the logos from the img tag of the class 'center-logos'
desc = soupPlate.find_all("span", "list-company")   # Find the descriptions from the span tag of the class 'list-company'

companyDict = {}

for i in range(len(logo)):
    companyDict[logo[i]['src']] = desc[i].get_text()

sortedTuple = sorted(companyDict.items(), key=lambda v: len(v[1]))      # sort by length of the description

for c in sortedTuple:
    print(c[0])
