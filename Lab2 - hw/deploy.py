from http_server import Server, request
import util

server = Server()


@server.register_route(verb='GET', route='/pilots')
def pilots_list():
    database = util.get_mongo_databse()
    return [*database['pilots'].find()], 200


@server.register_route(verb='POST', route='/pilots')
def pilots_create():
    database = util.get_mongo_databse()

    print(request.body)

    pilot = {}

    return pilot, 200


def main():
    server.start()


if __name__ == '__main__':
    main()
