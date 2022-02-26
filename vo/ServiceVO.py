class ServiceVO:
    def __init__(self, ip: str, name: str, enable: bool = True, port:int = 0):
        self.ip = ip
        self.name = name
        self.enable = enable
        self.port = port
        self.viewName = self.name+"-"+self.ip
