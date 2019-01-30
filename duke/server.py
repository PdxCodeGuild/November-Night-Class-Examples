from http.server import HTTPServer

from request_handler import RequestHandler

class Server:
    def __init__(self, server_address, routes):
        RequestHandler.add_routes(routes)
        self.httpd = HTTPServer(server_address, RequestHandler)

    def run(self):
        self.httpd.serve_forever()