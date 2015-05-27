import requests
import json


class Group():
    lights = None
    name = None

    def __init__(self, name, lights):
        self.name = name
        self.lights = lights

    def get_bridges(self):
        bridges = []

        for i in self.lights:
            bridges.append(i.bridge)

        return list(set(bridges))

    def update(self, data):
        res = []
        for bridge in self.get_bridges():
            path = '{prefix}/groups/{id}/action'.format(prefix=bridge.prefix, id=bridge.get_group(self.name))
            r = requests.put(path, json.dumps(data))
            res.append((r.status_code, json.loads(r.text)))

        return res
