import json
import time
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return json.dumps({'Hello': 'World'})

@app.route('/products/<id>')
def hello(id):
    time.sleep(2)
    return json.dumps({
        'id': id,
        'name': 'Pickled Eggs (Pallet)',
        'price': 12389.3218492819321
    })