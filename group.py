class Group():
    lights = None

    def __init__(self, lights):
        self.lights = lights

    def get_bridges(self):
        bridges = []

        for i in self.lights:
            bridges.append(i.bridge)

        return list(set(bridges))

    def update(self, data):
        for bridge in self.get_bridges():
            path = '{prefix}/groups/{id}/state'.format(prefix=bridge.prefix, id=self.group_id)

        print path
        print json.dumps(data)
        res = requests.put(path, json.dumps(data))
        return res.status_code, json.loads(res.text)
