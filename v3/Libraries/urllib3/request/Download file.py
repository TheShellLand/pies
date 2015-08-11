import urllib3.request


url = 'skynet.xyz'
file_to_get = 'robots.txt'

file = urllib3.PoolManager().request('GET', url + '/' + file_to_get, preload_content=False)