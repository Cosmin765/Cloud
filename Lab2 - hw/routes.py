import bson

from http_server import Server, request
import util
from config import *

server = Server()


def pilots_collection_get():
    database = util.get_mongo_database()
    return [*map(util.serialize_item, database['pilots'].find())], 200


def pilots_item_get(pilot_id):
    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        return 'bad id format', 400

    database = util.get_mongo_database()
    pilot = database['pilots'].find_one({'_id': pilot_id})

    if pilot is None:
        return "Not Found", 404

    return util.serialize_item(pilot), 200


@server.register_route(verb='GET', route='/pilots')
def pilots_get():
    pilot_id = request.args and request.args.get('id')
    if pilot_id:
        return pilots_item_get(pilot_id)
    else:
        return pilots_collection_get()


def pilots_collection_post():
    database = util.get_mongo_database()
    pilot = request.body

    if not util.validate_schema(pilot, PILOT_SCHEMA):
        return f'schema not met: {util.stringify_schema(PILOT_SCHEMA)}', 400

    database['pilots'].insert_one(pilot)
    return util.serialize_item(pilot), 201


def pilots_item_post(pilot_id):
    pilot = request.body

    if not util.validate_schema(pilot, PILOT_SCHEMA):
        return f'schema not met: {util.stringify_schema(PILOT_SCHEMA)}', 400

    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        return 'bad id format', 400

    database = util.get_mongo_database()
    if database['pilots'].find_one({'_id': pilot_id}):
        return 'pilot with this id already exists', 409

    return 'Not found', 404


@server.register_route(verb='POST', route='/pilots')
def pilots_post():
    pilot_id = request.args and request.args.get('id')
    if pilot_id:
        return pilots_item_post(pilot_id)
    else:
        return pilots_collection_post()


def pilots_collection_put():
    return 'Method Not Allowed', 405


def pilots_item_put(pilot_id):
    database = util.get_mongo_database()

    update_dict = {key: request.body[key] for key in PILOT_SCHEMA
                   if key in request.body}

    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        return 'bad id format', 400

    if database['pilots'].find_one({'_id': pilot_id}) is None:
        return 'Not Found', 404

    database['pilots'].replace_one({'_id': pilot_id}, update_dict)
    return 'success', 200


@server.register_route(verb='PUT', route='/pilots')
def pilots_put():
    pilot_id = request.args and request.args.get('id')
    if pilot_id:
        return pilots_item_put(pilot_id)
    else:
        return pilots_collection_put()


def pilots_collection_delete():
    return 'Method Not Allowed', 405


def pilots_item_delete(pilot_id):
    database = util.get_mongo_database()

    try:
        pilot_id = bson.ObjectId(pilot_id)
    except (TypeError, bson.errors.InvalidId):
        return 'bad id format', 400

    if database['pilots'].find_one({'_id': pilot_id}) is None:
        return 'Not Found', 404

    database['pilots'].delete_one({'_id': pilot_id})
    return 'success', 200


@server.register_route(verb='DELETE', route='/pilots')
def pilots_delete():
    pilot_id = request.args and request.args.get('id')
    if pilot_id:
        return pilots_item_delete(pilot_id)
    else:
        return pilots_collection_delete()
