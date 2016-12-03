#!/usr/bin/env python
# -*- coding: utf8 -*-

from datetime import datetime
import elasticsearch
import json
import os
import sys

es_server = 'http://10.0.2.149:9200'
es = elasticsearch.Elasticsearch([es_server])

script_path = os.path.realpath(__file__)
working_path = os.path.split(script_path)[0]

ES_TYPE = 'data_feed'
ES_INDEX = 'kl'


def main():
    if sys.argv[1]:
        path_file = os.path.join(working_path, sys.argv[1])

        if os.path.isfile(path_file):

            if os.path.splitext(path_file)[1] == '.json':
                with open(path_file, 'r') as f:
                    data = json.load(f)

                print('Importing:', path_file, '(', int(os.stat(path_file).st_size / 1024 / 1024), 'MB', ')')
                es.index(index=ES_INDEX, doc_type=ES_TYPE, body=data)

    else:

        for path, subdirs, files in os.walk(working_path):

            for file in files:
                path_file = os.path.join(path, file)

                if os.path.isfile(path_file):

                    if os.path.splitext(path_file)[1] == '.json':
                        # ES_INDEX = os.path.splitext(file)[0]

                        with open(path_file, 'r') as f:
                            data = json.load(f)

                        print('Importing:', file, '(', int(os.stat(path_file).st_size / 1024 / 1024), 'MB', ')')
                        es.index(index=ES_INDEX, doc_type=ES_TYPE, body=data)


if __name__ == "__main__":
    main()
