from http_server import Server

server = Server()


@server.register_route()
def mesaj():
    return {'mesaj': 'salut'}, 200


def main():
    server.start()


if __name__ == '__main__':
    main()
