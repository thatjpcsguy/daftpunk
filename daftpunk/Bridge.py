import requests
import json


class Bridge():
    ip = None
    user = None
    prefix = None

    def __init__(self, ip, user):
        self.ip = ip
        self.user = user
        self.prefix = "http://{ip}/api/{user}".format(ip=self.ip, user=self.user)

    def get_info(self):
        res = requests.get(self.prefix)
        return res.status_code, json.loads(res.text)

if __name__ == '__main__':
    b = Bridge("10.0.1.50", "newdeveloper")

    # print b.prefix
    # print b.get_info()
