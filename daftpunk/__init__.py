import json
import time

from colour import Color

from daftpunk.Light import Light
from daftpunk.Group import Group
from daftpunk.Bridge import Bridge


class DaftPunk():
    bridges = {}
    lights = {}
    sleep = None
    groups = {}
    name = None

    def __init__(self, config):
        with open(config) as data_file:
            config = json.load(data_file)

        self.name = config["name"]
        #read the config and set the various parts
        self.sleep = config["sleep"]
        self.transitiontime = config["transitiontime"]

        for i in config["bridges"]:
            self.bridges[i] = Bridge(config["bridges"][i]["ip"], config["bridges"][i]["user"])

        for i in config["lights"]:
            try:
                self.lights[i] = Light(self.bridges[config["lights"][i]["bridge"]], config["lights"][i]["id"], config["lights"][i]["x"], config["lights"][i]["y"])
            except:
                self.lights[i] = Light(self.bridges[config["lights"][i]["bridge"]], config["lights"][i]["id"])

        x = 1
        for i in config["groups"]:
            lights = []
            for j in config["groups"][i]:
                lights.append(self.lights[j])
            self.groups[i] = Group(i, lights, x if x <= 16 else None)
            x += 1

    # returns the ID of the line (1-7, A-G)
    def group_id(self, line):
        return self.groups[line]

    def bulb_id(self, bulb):
        return self.lights[bulb]

    def reset(self):
        self.on(0, True, True)
        self.brightness(0, 254, True)
        self.color(0, 0, True)

    def get(self, id):
        if id in self.lights.keys():
            return self.lights[id]
        elif id in self.groups.keys():
            return self.groups[id]

    def update(self, id, data):
        bulb = self.get(id)
        x = bulb.update(data)
        time.sleep(self.sleep)
        return x

    def colour(self, bulb, color, brightness=False, on=True, transitiontime=None):
        if type(color) == str:
            if color == "white":
                return self.saturation(bulb, 0)

            h, s, l = Color(color).get_hsl()

        data = {
            "transitiontime": self.transitiontime if not transitiontime else transitiontime,
            "hue": int(h*65000),
            "sat": int(s*254)
        }

        if on:
            data["on"] = on

        return self.update(bulb, data)

    def on(self, bulb, on):
        data = {
            "transitiontime": self.transitiontime,
            "on": on,
            "sat": 254,
            "bri": 254
        }

        return self.update(bulb, data)

    def brightness(self, bulb, bri):
        data = {
            "transitiontime": self.transitiontime,
            "bri": bri
        }

        return self.update(bulb, data)

    def saturation(self, bulb, sat):
        data = {
            "transitiontime": self.transitiontime,
            "sat": sat
        }

        return self.update(bulb, data)

    def wave(self, bulb, off=False):
        data = {
            "transitiontime": self.transitiontime,
            "effect": "colorloop" if off else "none",
            "sat": 254
        }

        return self.update(bulb, data)

    def siren(self):
        while True:
            self.colour(0, "red")
            self.colour(0, "blue")

    def slink(self, region="SE"):
        s = 0
        while True:
            for i in "ABCDEFG" if region == "SE" else "XYZ":
                    for j in "1234567" if region == "SE" else "123":
                        if i == "B" and j == "7":
                            continue
                        # self.on(i+j, True)
                        self.colour(i+j, s, 254)
                        s += 1000
                        if s > 65000:
                            s = 0

    def slink_rows(self):
        s = 0
        while True:
            for i in "ABCDEFG":
                self.colour(i, s % 65000)
                s += 5000

    def slink_cols(self):
        s = 0
        while True:
            for i in "1234567":
                self.colour(i, s % 65000)
                s += 5000

    def flash(self):
        s = 0
        while True:
            self.colour(0, s % 65000)
            s += 50000

    def chessboard(self):
        x = 0
        while True:
            for i in "ABCDEFG":
                for j in "1234567":
                    if i + j == "B7":
                        x += 1
                        continue
                    if x % 2 == 0:

                        self.colour(i+j, "blue")
                    else:
                        self.colour(i+j, "purple")
                    x += 1

if __name__ == '__main__':
    d = DaftPunk("config/default.json")

    # d.colour("room", "purple")
    d.wave("room", True)
