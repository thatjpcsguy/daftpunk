class Group():
    lights = None

    def __init__(self, lights):
        self.lights = lights

    def get_bridges(self):
        bridges = []

        for i in self.lights:
            bridges.append(i.bridge)

        return list(set(bridges))
