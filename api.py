from daftpunk import DaftPunk
from interpreter import Interpreter
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
        res = command + " " + request.args.get('light') + " " + request.args.get('colour')

    return jsonify(app.i.parse_line(str(res)))


if __name__ == '__main__':
    parser.add_argument("-c", "--config", dest="config_file", help="which config file to use")
    args = parser.parse_args()

    app.d = DaftPunk(args.config_file)
    app.i = Interpreter(app.d)

    app.run(host="0.0.0.0", debug=True)
