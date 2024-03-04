import http.server
import io
import socketserver
import json


class CustomHandler(http.server.SimpleHTTPRequestHandler):
    MAPPING = {}

    @staticmethod
    def handler_404():
        return b'Not found', 404

    def _complete_request(self, handler):
        content, status_code = handler()

        self.send_response(status_code)

        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        out = io.TextIOWrapper(self.wfile)
        json.dump(content, out)

        out.detach()  # prevent from closing the file

    def do_GET(self):
        handler = self.MAPPING.get(('GET', self.path), self.handler_404)
        self._complete_request(handler)


class Server:
    def __init__(self, ip='0.0.0.0', port=8000):
        socketserver.TCPServer.allow_reuse_address = True
        self._httpd = socketserver.TCPServer((ip, port), CustomHandler)

    def start(self):
        print('Server listening...')
        self._httpd.serve_forever()

    @staticmethod
    def register_route(route=None, verb='GET'):
        def registerer(handler):
            nonlocal route
            if route is None:
                route = '/' + handler.__name__

            CustomHandler.MAPPING[(verb, route)] = handler
            return handler
        return registerer
