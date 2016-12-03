__author__ = 'eric'

import requests, json
from pprint import pprint

url = []
url.append('http://catalog.data.gov/harvest/object/6f52bb4e-0d67-40da-a8a7-a85fa157587d')
url.append('https://www.bing.com')
url.append('https://www.google.com')

r = requests.get(url[0])
pprint(r.text)