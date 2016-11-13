#!/usr/bin/env python3

import sys
import requests
import bs4
import re
import time, random

if len(sys.argv) > 1:
    url = sys.argv[1]


def get_urls(url):
    """Print links, status code, and content length from the requested page"""

    url_domain = url.split('/')
    url_parent = '/'.join(url_domain[:-1])
    request_timeout = random.randrange(3, 10)

    try:
        request = requests.get(url, timeout=request_timeout)
        body = request.content

        if 'Content-Length' in request.headers:
            print('[*] URL: {} [{}][{} B]'.format(url, request.status_code, request.headers['Content-Length']))
        else:
            print('[*] URL: {} [{}]'.format(url, request.status_code))

        links = bs4.BeautifulSoup(body, 'html.parser').find_all('a')

        for link in links:
            request_interval = random.randrange(1, 2)
            raw_link = link.get('href')

            if type(raw_link) is str:
                new_link = url_parent + raw_link

                try:
                    links_request = requests.get(new_link)
                    links_body = links_request.content
                    links_page = bs4.BeautifulSoup(links_body, 'html.parser')
                    if 'Content-Length' in links_request.headers:
                        print('[{1}] {0} [{3}][{2} B]'.format(raw_link,
                                                              links_request.status_code,
                                                              links_request.headers['Content-Length'],
                                                              links_page.body))
                    else:
                        print('[{1}] {0} [{2}]'.format(raw_link,
                                                       links_request.status_code,
                                                       links_page.title.string))
                        #print('[DEBUG] Headers: {}'.format(links_request.headers))

                except requests.exceptions.InvalidURL as err:
                    print('[!] [Invalid URL] {} {}'.format(new_link, err))
                except requests.packages.urllib3.exceptions.MaxRetryError as err:
                    print('[!] [Max retries exceeded with url] {} {}'.format(new_link, err))
                except requests.exceptions.ConnectionError as err:
                    print('[!] [Max retries exceeded with url] {} {}'.format(new_link, err))

            time.sleep(request_interval)

    except requests.exceptions.ConnectTimeout as err:
        print('[!] [Connection timed out] {} {}'.format(url, err))


def save_files():
    """Save the files downloaded"""


def main(url):
    """The main programming function"""

    get_urls(url)


if __name__ == "__main__":
    main(url)
