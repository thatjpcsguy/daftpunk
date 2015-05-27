
import time

from beautifulhue.api import Bridge
from light import Light
from group import Group
from colour import Color

import argparse

import json


class DaftPunk():
    bridges = {}
    lights = {}
    sleep = None
    groups = {}

    def __init__(self, config):
        with open(config) as data_file:
            config = json.load(data_file)

        #read the config and set the various parts
        self.sleep = config["sleep"]
        self.transitiontime = config["transitiontime"]

        for i in config["bridges"]:
            self.bridges[i] = Bridge(device={'ip': config["bridges"][i]["ip"]}, user={'name': config["bridges"][i]["user"]})

        for i in config["lights"]:
            self.lights[i] = Light(self.bridges[config["lights"][i]["bridge"]], config["lights"][i]["id"])

        self.groups = {"roof": Group([self.lights["roof1"], self.lights["roof2"]]), "room": Group([self.lights["roof1"], self.lights["roof2"], self.lights["lamp1"]])}

    def get_colour(self, colour):
        return int(Color(colour).hue * 65000)

    # returns the ID of the line (1-7, A-G)
    def group_id(self, line):
        return self.groups[line]

    def bulb_id(self, bulb):
        return self.lights[bulb]

    def reset(self):
        d.on(0, True, True)
        d.brightness(0, 254, True)
        d.color(0, 0, True)

    def get(self, id):
        if id == 0:
            return 0, True

        elif id in self.lights.keys():
            group = False
            try:
                bulb = self.bulb_id(id)
            except:
                bulb = None

        elif id in self.groups.keys():
            group = True
            bulb = self.line_id(id)

        return bulb, group

    def action(self, group=False):
        if group:
            return "action"
        else:
            return "state"

    def update(self, id, data):
        bulb, group = self.get(id)
        resource = {
            "which": bulb.light_id,
            "data": {self.action(group): data}
        }

        try:
            if group:
                x = self.bridge.group.update(resource)
            else:
                x = bulb.bridge.light.update(resource)
        except:
            "Error updating %s!" % id

        time.sleep(self.sleep)
        return x

    def colour(self, bulb, color, brightness=False, on=True, transitiontime=None):
        if type(color) == str:
            if color == "white":
                return self.saturation(bulb, 0)

            color = self.get_colour(color)

        data = {
            "transitiontime": self.transitiontime if not transitiontime else transitiontime,
            "hue": color,
            "sat": 254
        }

        if brightness:
            data["bri"] = brightness

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
            "effect": "colorloop" if not off else "none"
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
