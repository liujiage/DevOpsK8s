class LogVO:

    def __init__(self, id=None,createTime=None,userName=None,serviceName=None,version=None,versionBefore=None,nodes=None,port=None):
        self.id = id
        self.createTime = createTime
        self.userName = userName
        self.serviceName = serviceName
        self.version = version
        self.versionBefore = versionBefore
        self.nodes = nodes
        self.port = port
