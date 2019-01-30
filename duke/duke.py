import json
import requests

from response import Response
from server import Server 
from route import route

def hello_world(request):
    response = requests.get('http://worldclockapi.com/api/json/est/now')
    return Response(body=response.json())

def test_user(request):
    return Response(body={
        'username': 'bob',
        'email': 'bob@bob.bob.com',
        'location': 'The Dalles, Oregon'
    })

routes = [
    route('/', hello_world),
    route('/user', test_user),
]

if __name__ == '__main__':
    print('Initializing the server...')
    server_address = ('localhost', 8000)
    s = Server(server_address, routes)
    print(f'Duke running @ {server_address[0]}:{server_address[1]}...')
    s.run()