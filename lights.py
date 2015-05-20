
import time
import random
from beautifulhue.api import Bridge
from colour import Color
import argparse

class Light():
    bridge = None
    light_id = None

    def __init__(self, bridge, light_id):
        self.bridge = bridge
        self.light_id =light_id


class DaftPunk():
    bridges = None
    lights = None
    sleep = None
    lines = None

    def __init__(self, bridges, sleep = 1, transitiontime = 0):
        self.bridges = bridges
        self.sleep = sleep
        self.transitiontime = transitiontime

        self.lights = {
                        'E2': Light(bridges['SE'], 16), 
                        'G7': Light(bridges['SE'], 9), 
                        'G6': Light(bridges['SE'], 6), 
                        'G5': Light(bridges['SE'], 3), 
                        'G4': Light(bridges['SE'], 36), 
                        'G3': Light(bridges['SE'], 8), 
                        'G2': Light(bridges['SE'], 43), 
                        'G1': Light(bridges['SE'], 30), 
                        'A1': Light(bridges['SE'], 2), 
                        'A3': Light(bridges['SE'], 41), 
                        'A2': Light(bridges['SE'], 12), 
                        'A5': Light(bridges['SE'], 47), 
                        'A4': Light(bridges['SE'], 10), 
                        'A7': Light(bridges['SE'], 35), 
                        'A6': Light(bridges['SE'], 24), 
                        'E5': Light(bridges['SE'], 18), 
                        'C2': Light(bridges['SE'], 20), 
                        'E7': Light(bridges['SE'], 23), 
                        'E6': Light(bridges['SE'], 14), 
                        'C7': Light(bridges['SE'], 1), 
                        'C6': Light(bridges['SE'], 46), 
                        'E3': Light(bridges['SE'], 7), 
                        'C4': Light(bridges['SE'], 42), 
                        'C3': Light(bridges['SE'], 29), 
                        'E4': Light(bridges['SE'], 21), 
                        'C1': Light(bridges['SE'], 38), 
                        'F1': Light(bridges['SE'], 37), 
                        'F2': Light(bridges['SE'], 33), 
                        'F3': Light(bridges['SE'], 26), 
                        'F4': Light(bridges['SE'], 44), 
                        'F5': Light(bridges['SE'], 28), 
                        'F6': Light(bridges['SE'], 15), 
                        'F7': Light(bridges['SE'], 31), 
                        'E1': Light(bridges['SE'], 27), 
                        'B4': Light(bridges['SE'], 32), 
                        'B5': Light(bridges['SE'], 5), 
                        'B6': Light(bridges['SE'], 22), 
                        'C5': Light(bridges['SE'], 45), 
                        'B2': Light(bridges['SE'], 25), 
                        'B3': Light(bridges['SE'], 13), 
                        'D6': Light(bridges['SE'], 11), 
                        'D7': Light(bridges['SE'], 17), 
                        'D4': Light(bridges['SE'], 40), 
                        'D5': Light(bridges['SE'], 4), 
                        'D2': Light(bridges['SE'], 39), 
                        'D3': Light(bridges['SE'], 19), 
                        'D1': Light(bridges['SE'], 34), 
                        'B1': Light(bridges['SE'], 48),

                        'X1': Light(bridges['NW'], 11),
                        'X2': Light(bridges['NW'], 12),
                        'X3': Light(bridges['NW'], 15),
                        'Y1': Light(bridges['NW'], 16),
                        'Y2': Light(bridges['NW'], 18),
                        'Y3': Light(bridges['NW'], 19),
                        'Z1': Light(bridges['NW'], 13),
                        'Z2': Light(bridges['NW'], 14),
                        'Z3': Light(bridges['NW'], 17)

                    }

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
                bulb = None

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
                'which': bulb.light_id,
                'data':{self.action(group): data}
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

    def colour(self, bulb, color, brightness=False, on=True):
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

        if brightness:
            data['bri'] = brightness

        if on:
            data['on'] = on

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


    def slink(self, region="SE"):
        s = 0
        while True:
            for i in 'ABCDEFG' if region == "SE" else 'XYZ':
                    for j in '1234567' if region == "SE" else '123':
                        if i == 'B' and j == '7':
                            continue
                        # self.on(i+j, True)
                        self.colour(i+j, s, 254)
                        s += 2000
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
    bridge = {}
    bridge["NW"] = Bridge(device={'ip':'10.117.109.22'}, user={'name':'newdeveloper'})
    bridge["SE"] = Bridge(device={'ip':'10.117.108.150'}, user={'name':'newdeveloper'})

    d = DaftPunk(bridge, sleep = .2, transitiontime=0)

    d.slink("SE")






