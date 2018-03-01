import asyncio
import requests
import re
import logging
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# logging.basicConfig(level=logging.DEBUG)


class Parser:

    def __init__(self, url):
        """Given a url, build a list of urls"""

        self.url = url
        self.tags = {}
        self.queues = {}
        self.loop = asyncio.get_event_loop()

        coros = [asyncio.ensure_future(self.__starter(self.url))]
        futures = [self.loop.run_until_complete(c) for c in coros]
    
    async def __starter(self, url):
        """This is the starter function to begin the async loop"""

        q = asyncio.Queue()
        q.put_nowait(url)
        self.queues['url'] = q
        coros = [await asyncio.ensure_future(self.__requester(q))]    

    async def __requester(self, queue):
        """This function will send requests for each url inside the queue"""

        q = asyncio.Queue()

        while not queue.empty():
            url = await queue.get()
            req = requests.get(url)
            q.put_nowait(req)

        self.queues['request'] = q
        coros = [await asyncio.ensure_future(self.__content(q))]
    
    async def __content(self, queue):
        """This function will build a queue of the contents from the requests"""

        q = asyncio.Queue()

        while not queue.empty():
            req = await queue.get()
            content = req.content
            q.put_nowait(content)
        
        self.queues['content'] = q
        coros = [await asyncio.ensure_future(self.__tags(q))]
        
    async def __tags(self, queue, tag='a'):
        """This function will get the tags from body of the contents
        By default the tag it will look for is <a>
        """

        q = asyncio.Queue()

        while not queue.empty():
            content = await queue.get()
            html_parser = 'html.parser'
            soup = BeautifulSoup(content, html_parser)
            q.put_nowait(soup)

            tags = []
            for a in soup.find_all('a'):
                tags.append(a)
            
            # host = urlparse(self.url).netloc
            self.tags[self.url] = tags
        
        self.queues['soup'] = q
    
    def tag(self, tag):
        """Return all tags for a search"""

        queue = self.queues['soup']

        while not queue.empty():
            soup = queue.get()

            for a in soup.find_all('a'):
                if tag:
                    print('{}'.format(a))

if __name__ == "__main__":
    url = ''
    parse_this = Parser(url)

    for tag in parse_this.tags[url]:
        print('{}\n'.format(tag))

