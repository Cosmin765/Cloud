import pymongo
import functools


@functools.lru_cache()
def get_mongo_database():
    return pymongo.MongoClient(host='localhost', port=27017)['formula1']


def serialize_item(item):
    item['_id'] = str(item['_id'])
    return item
