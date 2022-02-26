from vo.LogVO import LogVO
from vo.ServiceVO import ServiceVO


class DeployVO:
    def __init__(self, cmd, service: LogVO):
        self.cmd = cmd
        self.service = service
