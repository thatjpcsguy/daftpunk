
import time
import random
from beautifulhue.api import Bridge
from colour import Color
import argparse

class DaftPunk():
    bridge = None
    lights = None
    sleep = None
    lines = None

    def __init__(self, bridge, sleep = 1, transitiontime = 0):
        self.bridge = bridge
        self.sleep = sleep
        self.transitiontime = transitiontime
        self.lights = {'E2': 16, 'G7': 9, 'G6': 6, 'G5': 3, 'G4': 36, 'G3': 8, 'G2': 43, 'G1': 30, 'A1': 2, 'A3': 41, 'A2': 12, 'A5': 47, 'A4': 10, 'A7': 35, 'A6': 24, 'E5': 18, 'C2': 20, 'E7': 23, 'E6': 14, 'C7': 1, 'C6': 46, 'E3': 7, 'C4': 42, 'C3': 29, 'E4': 21, 'C1': 38, 'F1': 37, 'F2': 33, 'F3': 26, 'F4': 44, 'F5': 28, 'F6': 15, 'F7': 31, 'E1': 27, 'B4': 32, 'B5': 5, 'B6': 22, 'C5': 45, 'B2': 25, 'B3': 13, 'D6': 11, 'D7': 17, 'D4': 40, 'D5': 4, 'D2': 39, 'D3': 19, 'D1': 34, 'B1': 48}
        self.lines = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 'A': 8, 'B': 9, 'C': 10, 'D': 11, 'E': 12, 'F': 13, 'G': 14, 'frame4': 15, 'frame3': 16}

    def get_colour(self, colour):
        return int(Color(colour).hue * 65000)

    # returns the ID of the line (1-7, A-G)
    def line_id(self, line):
        return self.lines[line]

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
                bulb = 100

        elif id in self.lines.keys():
            group = True
            bulb = self.line_id(id)

        return bulb, group


    def action(self, group=False):
        if group:
            return 'action'
        else:
            return 'state'

    def update(self, id, data):
        bulb, group = self.get(id)
        resource = {
                'which': bulb,
                'data':{self.action(group): data}
                }

        try:
            if group:
                x = self.bridge.group.update(resource)
            else:
                x = self.bridge.light.update(resource)
        except:
            "Error updating %s!" % id
     
        time.sleep(self.sleep)
        return x

    def colour(self, bulb, color):
        if type(color) == str:
            if color == "white":
                self.saturation(bulb, 0)
                return

            color = d.get_colour(color)

        data = {
            'transitiontime': self.transitiontime,
            'hue': color,
            'sat': 254
        }

        print self.update(bulb, data)

    def on(self, bulb, on):
        data = {
                'transitiontime': self.transitiontime,
                'on': on,
                'sat': 254,
                'bri': 254
                }

        print self.update(bulb, data)

    def brightness(self, bulb, bri):
        data = {
                'transitiontime': self.transitiontime,
                'bri': bri
                }

        print self.update(bulb, data)


    def saturation(self, bulb, sat):
        data = {
                'transitiontime': self.transitiontime,
                'sat': sat
                }

        print self.update(bulb, data)


    def wave(self, bulb):
        data = {
                'transitiontime': self.transitiontime,
                'effect': 'colorloop'
                }

        print self.update(bulb, data)


    def siren(self):
        while True:
            self.colour(0, 'red')
            self.colour(0, 'blue')


    def slink(self):
        s = 0
        while True:
            for i in 'ABCDEFG':
                for j in '1234567':
                    if i == 'B' and j == '7':
                        continue
                    self.colour(i+j, s)
                    s += 1000
                    if s > 65000:
                        s = 0  

    def slink_rows(self):
        s = 0
        while True:
            for i in 'ABCDEFG':
                self.colour(i, s % 65000)
                s += 5000                  

    def slink_cols(self):
        s = 0
        while True:
            for i in '1234567':
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
             for i in 'ABCDEFG':
                 for j in '1234567':
                     if i + j == "B7":
                         x += 1
                         continue
                     if x % 2 == 0:
                         self.colour(i+j, "blue")
                     else:
                         self.colour(i+j, "purple")
                     x += 1




if __name__ == '__main__':
    d = DaftPunk(Bridge(device={'ip':'10.117.108.150'}, user={'name':'newdeveloper'}), sleep = .8, transitiontime=0)

    d.slink()
