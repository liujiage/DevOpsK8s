import sys

import ldap

from common.ConfigUtils import getConfig, LDAP_SERVER, LDAP_DOMAIN, LDAP_ENABLE

'''
@Function Authentication through LDAP
@Author Jiage
@2022-02-02
'''


class LdapService:
    def __init__(self, app):
        self.config = {}
        self.ldapServer = ""
        self.ldapDomain = ""
        self.ldapEnable = 0
        self.ldapConn = None
        self.app = app
        self.connect()

    '''
    @Function connect to the LDAP server
    @Author Jiage
    @2022-02-02
    '''

    def connect(self):
        # get config
        self.config = getConfig()
        self.ldapServer = self.config.get(LDAP_SERVER)
        self.ldapDomain = self.config.get(LDAP_DOMAIN)
        self.ldapEnable = int(self.config.get(LDAP_ENABLE))
        self.ldapConn = ldap.initialize(self.ldapServer)

    '''
    @Function check the user and password whether correct
    @Author Jiage
    @2022-02-02
    '''

    def isAuth(self, userName, password):
        try:
            # check parameters whether illegal
            if userName is None or len(userName) == 0 or password is None or len(password) == 0: return False
            self.connect()
            # if ldapEnable = 0. Disable ldap authentication
            if self.ldapEnable == 0: return True
            userId = '{0}{1}'.format(userName, self.ldapDomain)
            # connect to ldap server do authentication
            self.ldapConn.simple_bind_s(userId, password)
            return True
        except ldap.SERVER_DOWN as err:
            print("Can not connect to the LDAP server!", err)
        except ldap.INVALID_CREDENTIALS as err:
            print("User or password is not correct!", err)
        except:
            print("Unknown error!", sys.exc_info()[0])
        return False
