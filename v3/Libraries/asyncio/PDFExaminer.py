import re
import requests
import logging
import asyncio
import json
from urllib.parse import urlparse
from bs4 import BeautifulSoup, SoupStrainer

logging.basicConfig(level=logging.DEBUG)


class PDFExaminer:
    def __init__(self, url):

        self.url = url
        self.tasks = []
        self.json = []
        self.loop = asyncio.get_event_loop()

        coros = [asyncio.ensure_future(self.__get_first_page(self.url))]
        futures = [self.loop.run_until_complete(c) for c in coros]

        logging.debug('Finished __get_first_page: {}'.format(futures))
        logging.debug('Finished __get_first_page: {} json objects'.format(len(self.json)))

    async def __get_first_page(self, url):

        logging.debug('Running: __get_first_page(), on {}'.format(url))

        req = requests.get(url)
        req_q = asyncio.Queue()
        req_q.put_nowait(req)

        coros = [await asyncio.ensure_future(self.__get_first_page_a(req_q))]

        [logging.debug('Finished: __get_first_page: {}'.format(c)) for c in coros]

    async def __get_first_page_a(self, queue):

        logging.debug('Running: __get_first_page_a()')

        # host = urlparse(self.url).netloc

        while not queue.empty():

            req = await queue.get()
            content = req.content

            if req.status_code == 200:

                tag = 'a'
                # Search for <a> tags containing 'pdfsearch.php'
                tag = SoupStrainer(tag, href=re.compile('pdfsearch.php'))
                parsed = BeautifulSoup(content, 'html.parser', parse_only=tag)

                # all the href's
                hrefs = [t['href'] for t in parsed]

                # pdfsearch.php?hash=8108fb536c55ef61d58603360f42296f
                regex = '(?<=pdfsearch[\.]php[\?]hash=)[a-fA-F0-9]*'
                regex = re.compile(regex)

                md5_q = asyncio.Queue()
                for h in hrefs:
                    m = re.findall(regex, h)
                    if len(m) > 0:
                        md5_q.put_nowait(m[0])

                coros = [await asyncio.ensure_future(self.__get_second_page(md5_q))]

                [logging.debug('Finished: __get_first_page_a: {}'.format(c)) for c in coros]

            else:
                raise logging.error(req.status_code)

    async def __get_second_page(self, queue):

        logging.debug('Running: __get_second_page()')

        while not queue.empty():

            md5 = await queue.get()
            # Old URL for file data info in HTML
            url = 'https://www.malwaretracker.com/pdfdata.php?md5=' + md5 + '&type=document'
            # New URL for file data in JSON!
            url = 'https://www.pdfexaminer.com/pdfapirep.php?type=json&md5=' + md5
            req = requests.get(url)
            json_content = req.content
            json_content = json.loads(req.content)

            self.json.append(json_content)

            logging.debug('Finished: __get_second_page: {}'.format(md5))


r = PDFExaminer('https://www.pdfexaminer.com/pdfrecent.php')

