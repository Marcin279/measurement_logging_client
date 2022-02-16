from typing import List


class Client:
    def __init__(self, url: str, port: str, endpoints: List):
        self.url: str = url
        self.port: str = port
        self.endpoints: List = endpoints
