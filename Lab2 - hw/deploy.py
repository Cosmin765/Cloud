import bson

from http_server import Server, request
import util

server = Server()


def pilots_list():
    database = util.get_mongo_database()
    return [*map(util.serialize_item, database['pilots'].find())], 200


def pilots_get(pilot_id):
    database = util.get_mongo_database()
    pilot = database['pilots'].find_one({'_id': bson.ObjectId(pilot_id)})

    if pilot is None:
        return "Not found", 404

    return util.serialize_item(pilot), 200


@server.register_route(verb='GET', route='/pilots')
def pilots_get_root():
    pilot_id = request.args and request.args.get('id')
    if pilot_id:
        return pilots_get(pilot_id)
    else:
        return pilots_list()


@server.register_route(verb='POST', route='/pilots')
def pilots_create():
    # TODO: one more request for post
    database = util.get_mongo_database()
    collection = database['pilots']

    pilot = request.body

    schema = {
        'first_name': str,
        'last_name': str,
        'score': int
    }

    if not util.validate_schema(pilot, schema):
        return f'schema not met: {util.stringify_schema(schema)}', 400

    collection.insert_one(pilot)
    return util.serialize_item(pilot), 201


@server.register_route(verb='PUT', route='/pilots/<id>')
def pilots_update():
    database = util.get_mongo_database()
    return [*map(util.serialize_item, database['pilots'].find())], 200


@server.register_route(verb='DELETE', route='/pilots/<id>')
def pilots_update():
    # TODO: 2 requests - delete collection and delete one item
    database = util.get_mongo_database()
    return [*map(util.serialize_item, database['pilots'].find())], 200


def main():
    server.start()


if __name__ == '__main__':
    main()
