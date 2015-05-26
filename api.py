from lights import DaftPunk
from flask import Flask, jsonify, request

from argparse import ArgumentParser

app = Flask(__name__)
parser = ArgumentParser()

@app.route('/')
def hello_world():
    return 'Welcome to Daft Punk!'


@app.route('/<command>')
def command(command):
    if command == "colour":
        res = app.d.colour(request.args.get('light'), str(request.args.get('colour')))
    # elif command == "on":
    #     res = app.d.on(request.args.get('light'), bool(request.args.get('on')))

    return jsonify(res)


if __name__ == '__main__':
    parser.add_argument("-c", "--config", dest="config_file", help="which config file to use")
    args = parser.parse_args()

    app.d = DaftPunk(args.config_file)

    app.run(host="0.0.0.0", debug=True)
