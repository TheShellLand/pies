import asyncio
import logging
import datetime

from helpers.elasticsearch_helper import es_wrapper
from helpers.elasticsearch_helper import get_indice
from helpers.elasticsearch_helper import get_alias


logging.basicConfig(level=logging.ERROR)


async def main():
    hosts = ['']

    es = await es_wrapper(hosts)
    all = await get_alias(es)

    for alias in all:
        indices = await get_indice(es, alias)

        creation_date = indices[alias]['settings']['index']['creation_date']
        creation_date = int(creation_date)

        # month old
        month = datetime.timedelta(days=30)
        today = datetime.datetime.today()
        past = today - month
        epoch = past - datetime.datetime.utcfromtimestamp(0)
        delete_older = int(epoch.total_seconds()) * 1000

        if creation_date < delete_older:
            # delete index
            # es.indices.delete(alias, ignore=[400, 404])
            es.indices.delete(alias)
            print('deleted', alias)

    return


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
