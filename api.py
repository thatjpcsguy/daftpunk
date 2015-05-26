from lights import DaftPunk
from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to Daft Punk!'


@app.route('/colour/<l>/<c>')
def change_colour(l, c):
    x = app.d.colour(l, str(c.strip()))
    return json.dumps(x)


if __name__ == '__main__':
    app.d = DaftPunk("sydney.json")
    app.run(debug=True)
