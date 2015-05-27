import requests
import json


class Light():
    bridge = None
    light_id = None

    def __init__(self, bridge, light_id):
        self.bridge = bridge
        self.light_id = light_id

    def update(self, data):
        path = '{prefix}/lights/{id}/state'.format(prefix=self.bridge.prefix, id=self.light_id)

        print path
        print json.dumps(data)
        r = requests.put(path, json.dumps(data))
        res = [(r.status_code, json.loads(r.text))]
        return res
