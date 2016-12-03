#!/usr/bin/env python3

import sys
import requests



def downloader(url):
	file_name = url.split('/')[-1].split('?')[0]
	print('URL: {}'.format(url))
	print('Filename: {}'.format(file_name))

	f = open(file_name, 'wb')

	r = requests.get(url, stream=True)
	#print('Headers: {}'.format(r.headers))
	file_size = r.headers['Content-Length']
	print('Size (bytes): {}'.format(file_size))

	bytes_downloaded = 0
	block_size = 8192
	for buffer in r.iter_content(chunk_size=block_size):
		if not buffer:
			break

		bytes_downloaded += len(buffer)
		f.write(buffer)
		progress_bar = 100
		done = int(progress_bar * bytes_downloaded / int(file_size))
		percent = bytes_downloaded / int(file_size)
		remaining = int(file_size) - bytes_downloaded
		sys.stdout.write('\r{2:.0%}[{0}{1}]100%'.format('#' * done, ' ' * (progress_bar - done), percent))
	
	f.close()


# main
downloader(str(sys.argv[-1]))

