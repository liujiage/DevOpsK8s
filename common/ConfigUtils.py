import configparser
import os

'''
Shell command config
'''
EVN_SWITCH = "evn.switch"

PRE_DEPLOY_SERVICE = "pre.deploy.service"
PRE_SSHPASS = "pre.sshpass"
PRE_CLUSTER_SERVICE = "pre.cluster.service"
PRE_NODES_SERVICE = "pre.nodes.service"
PRE_SERVICES_SERVICE = "pre.services.service"
PRE_PODS_SERVICE = "pre.pods.service"
PRE_STATUS_SERVICE = "pre.status.service"
PRE_AUTO_SCALE_USAGE = "pre.auto.scale.usage"
PRE_AUTO_SCALE_ADJUST = "pre.auto.scale.adjust"
PRE_AUTO_ASSIGN_PODS = "pre.auto.assign.pods"

CUR_DEPLOY_SERVICE = "cur.deploy.service"
CUR_SSHPASS = "cur.sshpass"
CUR_CLUSTER_SERVICE = "cur.cluster.service"
CUR_NODES_SERVICE = "cur.nodes.service"
CUR_SERVICES_SERVICE = "cur.services.service"
CUR_PODS_SERVICE = "cur.pods.service"
CUR_STATUS_SERVICE = "cur.status.service"
CUR_AUTO_SCALE_USAGE = "cur.auto.scale.usage"
CUR_AUTO_SCALE_ADJUST = "cur.auto.scale.adjust"
CUR_AUTO_ASSIGN_PODS = "cur.auto.assign.pods"

EVN_DEVELOP_CONST = "dt"
EVN_TEST_CONST = "pre"
EVN_PRODUCT_CONST = "pro"

'''
LDAP authentication config
'''
LDAP_SERVER = "ldap.server"
LDAP_DOMAIN = "ldap.domain"
LDAP_ENABLE = "ldap.enable"

'''
Database config
'''
SQLITE_FILE = "sqlite.file"

'''
@function setting different environments
@Author Jiage
@Date 2021-08-20
@description 
   @see project/resources/config.properties
   evn.switch {dt|pre}
      dt is develop environment 
      pre is testing environment
      pro is product environment
'''


def getConfig():
    config = configparser.RawConfigParser()
    filePath = os.path.join(os.path.abspath(os.curdir), 'resources', 'config.properties')
    print("filePath " + filePath)
    config.read(filePath)
    # get shell command config
    cd = dict(config.items("SHELL_CONFIG"))
    # es = cd.get(EVN_SWITCH)
    # if (es == EVN_TEST_CONST):
    cd.setdefault(CUR_DEPLOY_SERVICE, cd.get(PRE_DEPLOY_SERVICE))
    cd.setdefault(CUR_SSHPASS, cd.get(PRE_SSHPASS))
    cd.setdefault(CUR_CLUSTER_SERVICE, cd.get(PRE_CLUSTER_SERVICE))
    cd.setdefault(CUR_NODES_SERVICE, cd.get(PRE_NODES_SERVICE))
    cd.setdefault(CUR_SERVICES_SERVICE, cd.get(PRE_SERVICES_SERVICE))
    cd.setdefault(CUR_PODS_SERVICE, cd.get(PRE_PODS_SERVICE))
    cd.setdefault(CUR_STATUS_SERVICE, cd.get(PRE_STATUS_SERVICE))
    cd.setdefault(CUR_AUTO_SCALE_USAGE, cd.get(PRE_AUTO_SCALE_USAGE))
    cd.setdefault(CUR_AUTO_SCALE_ADJUST, cd.get(PRE_AUTO_SCALE_ADJUST))
    cd.setdefault(CUR_AUTO_ASSIGN_PODS, cd.get(PRE_AUTO_ASSIGN_PODS))
    # get ldap config
    ld = dict(config.items("LDAP_CONFIG"))
    # get database config
    db = dict(config.items("DB_CONFIG"))
    rd = {**cd, **ld}
    rs = {**rd, **db}

    return rs
