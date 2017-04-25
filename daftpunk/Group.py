import requests
import json
import pickle
import os

class Group():
    lights = None
    group_id = None
    name = None

    def __init__(self, name, lights, group_id=None):
        self.name = name
        self.group_id = group_id
        self.lights = lights

        self.brightness = self.get_brightness()
        self.create()

    def get_brightness(self):
        if os.path.isfile('cache/%s_brightness.pickle' % self.group_id):
            return pickle.load(open('cache/%s_brightness.pickle' % self.group_id, "rb"))
        else:
            return 0
            
    def set_brightness(self, brightness):
        self.brightness = brightness
        return pickle.dump(self.brightness, open('cache/%s_brightness.pickle' % self.group_id, "wb"))

    def create(self, group_id=None):
        if group_id:
            self.group_id = group_id

        res = []
        for i in self.get_bridges():
            lights = []
            # find the light ids in this group on that bridge
            for j in self.lights:
                if j.bridge == i:
                    lights.append(str(j.light_id))

            path = '{prefix}/groups/{id}'.format(prefix=i.prefix, id=self.group_id)
            data = {
                "name": self.name,
                "lights": lights
            }
            r = requests.put(path, json.dumps(data))
            ro = json.loads(r.text)[0]
            # print ro['error']
            if 'error' in ro:
                path = '{prefix}/groups'.format(prefix=i.prefix)
                r = requests.post(path, json.dumps(data))
                ro = json.loads(r.text)[0]
                res.append((r.status_code, ro))
                group_id = int(ro['success']['id'])
            else:
                res.append((r.status_code, ro))

        return res

    def set_id(self, id):
        self.group_id = id

    def get_bridges(self):
        bridges = []
        for i in self.lights:
            bridges.append(i.bridge)
        return list(set(bridges))

    def update(self, data):
        res = []
        for bridge in self.get_bridges():
            path = '{prefix}/groups/{id}/action'.format(prefix=bridge.prefix, id=self.group_id)
            r = requests.put(path, json.dumps(data))
            res.append((r.status_code, json.loads(r.text)))

        return res

    # def __repr__(self):
    #     return "<Group "+ self.name + ">"
