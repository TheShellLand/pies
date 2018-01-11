# http://rosettacode.org/wiki/Respond_to_an_unknown_method_call#Python

class ElasticWrapper():

    def __init__(self, item):
        self.client = Elasticsearch(item, maxsize=100)        # max connections to each node

    def __getattr__(self, item):
        return getattr(self.client, item)
