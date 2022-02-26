import subprocess
import threading
import time
import re

import common.ConfigUtils as cf
from common.StrUtils import isEmpty
from services.ParseService import parseSampleResult
from services.dao.AutoScaleSettingDao import AutoScaleSettingDao

'''
@function auto scale services 
@Author Jiage
@Date 2022-02-21
'''
class AutoScaleService (threading.Thread):

    def __init__(self, _delay=10):
        threading.Thread.__init__(self)
        self.assDao = AutoScaleSettingDao()
        self.delay = _delay

    def run(self):
        print("AutoScaleService check nodes and scale setting...")
        while 1:
            try:
                # get auto scale setting from sqlite3 database
                setting = self.assDao.query()
                # check setting value
                if setting.miniSize > setting.maxSize or setting.miniSize <= 0 or setting.maxSize <= 0 or isEmpty(setting.deployName) or setting.memExc <= 0:
                    print("error setting.miniSize < setting.maxSize or setting.miniSize <= 0 or isEmpty("
                          "setting.deployName) or setting.memExc <= 0")
                    time.sleep(self.delay)
                    continue
                # get all node usage memory
                cmd, nodes = parseSampleResult(command=cf.CUR_AUTO_SCALE_USAGE, extendCommand=" "+setting.deployName), []
                with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1,
                                      universal_newlines=True) as p:
                    for line in iter(p.stdout.readline, ""):
                        nodes.append(re.sub(' +', ',', line.replace("\n", "").replace("Mi", "")).split(',')[2])
                # get current have been assign the number of pod
                cmd, assign_pod_nums = parseSampleResult(command=cf.CUR_AUTO_ASSIGN_PODS, extendCommand=" " + setting.deployName), 0
                with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1,
                                      universal_newlines=True) as p:
                    for line in iter(p.stdout.readline, ""):
                        line = re.sub(' +', ',', line.replace("/",",")).split(',')[2]
                        assign_pod_nums = int(line)
                        break
                # cal the node usage and auto scale setting
                nodes_sum = len(nodes)
                if assign_pod_nums != nodes_sum:
                    print("waiting for assign to be done!")
                    time.sleep(self.delay)
                    continue
                nodes_usage_total = 0
                for node in nodes:
                    nodes_usage_total = nodes_usage_total + int(node)
                real_size = round(nodes_usage_total / setting.memExc)
                if real_size <= 0:
                    real_size = 1
                if real_size > setting.maxSize:
                    real_size = setting.maxSize
                # check whether node size less then mini size
                if nodes_sum < setting.miniSize:
                    cmd = parseSampleResult(command=cf.CUR_AUTO_SCALE_ADJUST)
                    cmd = cmd.format(setting.deployName, str(setting.miniSize))
                    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1,
                                          universal_newlines=True):
                        pass
                    time.sleep(self.delay)
                    continue
                elif nodes_sum > setting.maxSize:
                    cmd = parseSampleResult(command=cf.CUR_AUTO_SCALE_ADJUST)
                    cmd = cmd.format(setting.deployName, str(setting.maxSize))
                    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1,
                                          universal_newlines=True):
                        pass
                    time.sleep(self.delay)
                    continue
                elif (setting.miniSize <= nodes_sum <= setting.maxSize) and (nodes_sum != real_size):
                    cmd = parseSampleResult(command=cf.CUR_AUTO_SCALE_ADJUST)
                    cmd = cmd.format(setting.deployName, str(real_size))
                    with subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, bufsize=1,
                                          universal_newlines=True):
                        pass
                    time.sleep(self.delay)
                    continue
                time.sleep(self.delay)
            except Exception as e:
                print(repr(e))
                time.sleep(self.delay)



