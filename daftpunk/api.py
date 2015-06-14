from daftpunk.DaftPunk import DaftPunk
from daftpunk.interpreter import Interpreter
from flask import Flask, jsonify, request, render_template
from argparse import ArgumentParser

app = Flask(__name__)
parser = ArgumentParser()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/colour')
def colour():
    res = "colour " + request.args.get('light') + " " + request.args.get('colour')
    return jsonify(app.i.parse_line(str(res)))


@app.route('/on')
def on():
    res = "on " + request.args.get('light') + " " + request.args.get('on')
    return jsonify(app.i.parse_line(str(res)))


@app.route('/get-name')
def get_name():
    return jsonify(data=app.i.d.name)


@app.route('/list-lights')
def list_lights():
    data = []
    for light in app.i.d.lights:
        data.append({"name": light, "x": app.i.d.lights[light].x_coord, "y": app.i.d.lights[light].y_coord})

    return jsonify(data=data)


def main():
    parser.add_argument("-c", "--config", dest="config_file", help="which config file to use")
    args = parser.parse_args()

    app.i = Interpreter(DaftPunk(args.config_file))

    app.run(host="0.0.0.0", debug=True)


if __name__ == '__main__':
    main()
