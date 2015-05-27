class Light():
    bridge = None
    light_id = None

    def __init__(self, bridge, light_id):
        self.bridge = bridge
        self.light_id = light_id
