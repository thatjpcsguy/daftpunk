from daftpunk import DaftPunk
from argparse import ArgumentParser


class Interpreter():
    def __init__(self, config):
        self.d = config

    def parse_line(self, line=""):
        line = line.split(' ')

        command = line[0]
        if command == "colour":
            return self.d.colour(line[1], line[2])
        elif command == "on":
            return self.d.on(line[1], True if line[2] == "True" else False)
        elif command == "brightness":
            return self.d.brightness(line[1], int(line[2]))
        elif command == "saturation":
            return self.d.saturation(line[1], int(line[2]))
        elif command == "wave":
            return self.d.wave(line[1], True if line[2] == "True" else False)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", dest="config_file", help="which config file to use")
    args = parser.parse_args()

    i = Interpreter(DaftPunk(args.config_file))

    d = raw_input("Command: ")
    while d:
        print i.parse_line(d)
        d = raw_input("Command: ")
