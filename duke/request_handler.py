from handlers import handle_request
from http.server import BaseHTTPRequestHandler

class RequestHandler(BaseHTTPRequestHandler):
    routes = None
    
    def do_GET(self):
        response = handle_request(self, self.routes)
        response.handle(self)

    def do_POST(self):
        response = handle_request(self, self.routes)
        response.handle(self)

    def do_PUT(self):
        response = handle_request(self, self.routes)
        response.handle(self)

    def do_PATCH(self):
        response = handle_request(self, self.routes)
        response.handle(self)

    def do_DELETE(self):
        response = handle_request(self, self.routes)
        response.handle(self)

    @staticmethod
    def add_routes(routes):
        RequestHandler.routes = routes