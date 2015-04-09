import time
import random
from beautifulhue.api import Bridge
from colour import Color

class DaftPunk():
    bridge = None
    lights = None
    sleep = None
    lines = None

    def __init__(self, bridge, sleep = 1):
        self.bridge = bridge
        self.sleep = sleep
        self.transitiontime = 1
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

        if group:
            x = self.bridge.group.update(resource)
        else:
            x = self.bridge.light.update(resource)

        time.sleep(self.sleep)
        return x

    def colour(self, bulb, color):
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
                'sat': 254
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

    # def chessboard(self):
    #     x = 0
    #     for i in 'ABCDEFG':
    #         for j in '1234567':
    #             x += 1




if __name__ == '__main__':

    d = DaftPunk(Bridge(device={'ip':'10.117.108.150'}, user={'name':'newdeveloper'}), sleep = 0.5)

    #d.wave(0)
    # d.on(0, True)
    # d.brightness(0, 254)

    # d.colour('G7', "orange")
    # d.colour('E', "blue")
    # d.colour('A4', "yellow")
    # d.blank()

    # while True:
    #     d.colour(0, "blue")
    #     d.colour(0, "red")

    d.colour(0, 'green')
    d.colour('frame4', "red")
    d.colour('frame3', "blue")
    d.colour('D4', 'purple')

    # frame1 = []
    # for i in 'ABCDEFG':
    #     for j in '1234567':
    #         if i == 'A' or i == 'G' or j == '1' or j == '7':
    #             continue
    #         if i == 'B' or i == 'F' or j == '2' or j == '6':
    #             continue
    #         if i == 'C':
    #             print i, j
    #             frame1.append(str(d.lights[i+j]))
    #         elif i == 'E':
    #             print i, j
    #             frame1.append(str(d.lights[i+j]))
    #         elif j == '3':
    #             print i, j
    #             frame1.append(str(d.lights[i+j]))
    #         elif j == '5':
    #             print i, j
    #             frame1.append(str(d.lights[i+j]))

    # print frame1


    # A1, B1, C1, D1, E1, F1, G1

    # A2,                     G2

    # A3,

    # A4, 

    # A5, 

    # A6,

    # A7, B7, C7, D7, E7, F7, G7


    # for i in 'ABCDEFG':
    #     for j in '1234567':
    #         d.colour(i+j, "yellow")
    #         d.saturation(i+j, 1)
    #     # d.on(i, True)
    #     # d.brightness(i, 254)
    #     d.colour(i, "red")


    # d.colour(0, "orange")

    # d.reset()

    # print d.colour.green
    # print d.colour.red
    # print d.colour.blue

    # d.saturation(0, 0, True)

    # hue = 0
    # d.bri(0, 255)
    # i = 0
    # while True:
    #     i += 1
    #     if i % 4 == 1:
    #         d.color((i%14)+1, red)
    #     elif i % 4 == 2:
    #         d.color((i%14)+1, green)
    #     elif i % 4 == 3:
    #         d.color((i%14)+1, purple)
    #     else:
    #         d.color((i%14)+1, blue)


