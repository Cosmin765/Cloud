import http.server
import io
import socketserver
import json


class Request:
    def __init__(self):
        self.body = None


request = Request()


class CustomHandler(http.server.BaseHTTPRequestHandler):
    MAPPING = {}

    @staticmethod
    def handler_404():
        return 'Not found', 404

    def _complete_request(self, handler):
        content_type = self.headers.get('content-type')
        content_length = self.headers.get('content-length')

        if content_type is not None and content_type != 'application/json':
            self.send_response(400)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'application/json accepted only')
            return

        request.body = content_type and json.loads(self.rfile.read(int(content_length)))

        try:
            content, status_code = handler()
        except Exception as exc:
            print(exc)
            content, status_code = 'Internal server error', 500

        self.send_response(status_code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        out_wrapper = io.TextIOWrapper(self.wfile)
        json.dump(content, out_wrapper)
        out_wrapper.detach()  # prevent from closing the file

    def do_GET(self):
        self._complete_request(self.MAPPING.get(('GET', self.path), self.handler_404))

    def do_POST(self):
        self._complete_request(self.MAPPING.get(('POST', self.path), self.handler_404))

    def do_PUT(self):
        self._complete_request(self.MAPPING.get(('PUT', self.path), self.handler_404))

    def do_DELETE(self):
        self._complete_request(self.MAPPING.get(('DELETE', self.path), self.handler_404))


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
