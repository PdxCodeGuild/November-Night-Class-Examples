import json

class InvalidResponseType(Exception):
    pass

class Response:
    def __init__(self, body, status_code=200, headers=[]):
        self.body = body
        self.status_code = status_code
        self.headers = headers

    def handle(self, request):
        request.send_response(self.status_code)

        if isinstance(self.body, dict): 
            request.send_header('Content-type', 'application/json')
            request.end_headers()

            request.wfile.write(bytes(json.dumps(self.body), "utf8"))
        elif isinstance(self.body, str):
            request.send_header('Content-type', 'text/plain')
            request.end_headers()

            request.wfile.write(bytes(self.body, "utf8"))
        else:
            raise InvalidResponseType
