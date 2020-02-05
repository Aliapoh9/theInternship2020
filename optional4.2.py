import requests
from bs4 import BeautifulSoup
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

page = requests.get("https://theinternship.io")
html = page.content
soupPlate = BeautifulSoup(html, features="html.parser")

logo = soupPlate.find_all("img", "center-logos")
desc = soupPlate.find_all("span", "list-company")

companyDict = {}

for i in range(len(logo)):
    companyDict[logo[i]['src']] = desc[i].get_text()

sortedTuple = sorted(companyDict.items(), key=lambda v: len(v[1]))

jsonDisplay = []

for c in sortedTuple:
    full = "https://theinternship.io/" + c[0]
    newDict = {}
    newDict['logo'] = full
    jsonDisplay.append(newDict)


def index(request):
    return Response("go to http://localhost:2434/companies")


def companiesList(request):
    return {'companies': jsonDisplay}


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('index', '/')
        config.add_route('companies', '/companies')
        config.add_view(index, route_name='index')
        config.add_view(companiesList, route_name='companies', renderer='json', request_method='GET')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 2434, app)
    server.serve_forever()