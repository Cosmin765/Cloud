import pymongo
import functools


@functools.lru_cache()
def get_mongo_database():
    return pymongo.MongoClient(host='localhost', port=27017)['formula1']


def validate_schema(body, schema):
    if schema is None:  # the field can be anything
        return True

    if isinstance(schema, list):
        for item_body, item_schema in zip(body, schema):
            if not validate_schema(item_body, item_schema):
                return False
    elif isinstance(schema, dict):
        for key in [*body.keys(), *schema.keys()]:
            if key not in schema:
                return False

            if key not in body:
                return False

            if not validate_schema(body[key], schema[key]):
                return False
    elif not isinstance(body, schema):
        return False

    return True


def stringify_schema(schema):
    if isinstance(schema, dict):
        result = {}
        for key in schema:
            result[key] = stringify_schema(schema[key])
    elif isinstance(schema, list):
        result = []
        for item in schema:
            result.append(stringify_schema(item))
    else:
        result = str(schema)

    return result


def serialize_item(item):
    item['_id'] = str(item['_id'])
    return item
