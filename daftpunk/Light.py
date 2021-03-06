import requests
import json


class Light():
    bridge = None
    light_id = None
    x_coord = None
    y_coord = None

    def __init__(self, bridge, light_id, x_coord=0, y_coord=0):
        self.bridge = bridge
        self.light_id = light_id
        self.x_coord = x_coord
        self.y_coord = y_coord

    def update(self, data):
        path = '{prefix}/lights/{id}/state'.format(prefix=self.bridge.prefix, id=self.light_id)

        print path
        print json.dumps(data)
        r = requests.put(path, json.dumps(data))
        res = [(r.status_code, json.loads(r.text))]
        return res
