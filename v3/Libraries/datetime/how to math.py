
def age(self):
    epoch = int(self.Elasticsearch.indices.get_settings(index=self.index)[self.index]['settings']['index'][
                    'creation_date']) // 1000
    delta = datetime.datetime.now() - datetime.datetime.fromtimestamp(epoch)
    seconds = delta.seconds
    days, seconds = seconds // 86400, seconds % 86400
    hours, seconds = seconds // 3600, seconds % 3600
    minutes, seconds = seconds // 60, seconds % 60
    return print('{} was created {} days {} hours {} minutes {} seconds ago\n'.format(
        self.index,
        days,
        hours,
        minutes,
        seconds
    ))
