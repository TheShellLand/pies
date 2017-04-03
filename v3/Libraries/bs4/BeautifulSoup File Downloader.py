import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

url = ''
file = ''

page = requests.get(url).content
links = BeautifulSoup(page, 'html.parser').find_all('a')


try:
    with open(file, 'r') as f:
        links = BeautifulSoup(f, 'html.parser').find_all('a')

    count = 0

    for image in links:
        href = image['href']

        if re.search('jpg', href, flags=re.I):
            print(href)
            count += 1

            name = href.split('/')[-1:][0]

            with open(name, 'wb') as download:
                download.write(requests.get(href).content)
                print('Saved ' + name)


    print(count)




except Exception as exc:
    print(exc)



