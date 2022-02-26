class AutoScaleSettingVO:
    def __init__(self, mini_size=1, max_size=1, mem_exc=0, deploy_name = ""):
        self.miniSize = mini_size
        self.maxSize = max_size
        self.memExc = mem_exc
        self.deployName = deploy_name
        self.operationResult = ""
