__author__ = 'eric'

import requests, json
from pprint import pprint

url = 'http://catalog.data.gov/harvest/object/6f52bb4e-0d67-40da-a8a7-a85fa157587d'


#page = requests.get(url)

pprint(page.json)