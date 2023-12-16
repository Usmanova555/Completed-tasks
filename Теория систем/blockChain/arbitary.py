import requests

class Arbitary:
    def __init__(self,url,payload):
        self.request = requests.get(url, params=payload)


