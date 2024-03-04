import pymongo
import functools


@functools.lru_cache()
def get_mongo_databse():
    return pymongo.MongoClient(host='localhost', port=27017)['formula1']
