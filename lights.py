import time
import random
from beautifulhue.api import Bridge


class Colour():
    purple = 52000
    blue = 46920
    green = 25500
    red = 0


class DaftPunk():
    bridge = None
    lights = None
    colour = None
    sleep = None
    lines = None

    def __init__(self, bridge):
        self.colour = Colour()
        self.bridge = bridge
        self.sleep = .4
        self.transitiontime = 1
        self.lights = {'E2': 16, 'G7': 9, 'G6': 6, 'G5': 3, 'G4': 36, 'G3': 8, 'G2': 43, 'G1': 30, 'A1': 2, 'A3': 41, 'A2': 12, 'A5': 47, 'A4': 10, 'A7': 35, 'A6': 24, 'E5': 18, 'C2': 20, 'E7': 23, 'E6': 14, 'C7': 1, 'C6': 46, 'E3': 7, 'C4': 42, 'C3': 29, 'E4': 21, 'C1': 38, 'F1': 37, 'F2': 33, 'F3': 26, 'F4': 44, 'F5': 28, 'F6': 15, 'F7': 31, 'E1': 27, 'B4': 32, 'B5': 5, 'B6': 22, 'C5': 45, 'B2': 25, 'B3': 13, 'D6': 11, 'D7': 17, 'D4': 40, 'D5': 4, 'D2': 39, 'D3': 19, 'D1': 34, 'B1': 48}
        self.lines = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, 'A': 8, 'B': 9, 'C': 10, 'D': 11, 'E': 12, 'F': 13, 'G': 14}

    # returns the ID of the line (1-7, A-G)
    def line_id(self, line):
        return self.lines[line]

    def bulb_id(self, bulb):
        return self.lights[bulb]


    def action(self, group=False):
        if group:
            return 'action'
        else:
            return 'state'

    def color(self, id, color, group=False):
        resource =  {
                    'which':id,
                    'data':{
                        self.action(group):{
                            'transitiontime': self.transitiontime,
                            'hue': color,
                            }
                        }
                    }

        print self.bridge.group.update(resource)
        time.sleep(self.sleep)

    def on(self, id, on, group=False):
        resource =  {
                    'which':id,
                    'data':{
                        self.action(group): {
                            'transitiontime': self.transitiontime,
                            'on': on,
                            }
                        }
                    }

        print self.bridge.group.update(resource)
        time.sleep(self.sleep)

    def brightness(self, id, bri, group=False):
        resource =  {
                    'which':id,
                    'data':{
                        self.action(group):{
                           'transitiontime': self.transitiontime,
                           'bri': bri
                           }
                        }
                    }

        print self.bridge.group.update(resource)
        time.sleep(self.sleep)

    def wave(self, id, group=False):
        resource =  {
                    'which':id,
                    'data':{
                        self.action(group):{
                            'transitiontime': self.transitiontime,
                            'effect': 'colorloop'
                            }
                        }
                    }

        print self.bridge.group.update(resource)
        time.sleep(self.sleep)



if __name__ == '__main__':

    d = DaftPunk(Bridge(device={'ip':'10.117.108.150'}, user={'name':'newdeveloper'}))

    #d.wave(0)
    # d.on(0, True)
    # d.brightness(0, 254)

    d.color(d.line_id('A'), d.colour.blue, group=True)

    d.color()


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


