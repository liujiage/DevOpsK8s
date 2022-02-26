import sys
import unittest

import ldap


def isCheck():
    try:
        password = "1111"
        if password is None or len(password) == 0:
            return False
        conn = ldap.initialize('ldap://120.50.46.117')
        res = conn.simple_bind_s(who="liujiage@mozone.lan", cred=password)
        print(res)
        return True
    except ldap.SERVER_DOWN as err:
        print("Can not connect to the LDAP server!", err)
    except ldap.INVALID_CREDENTIALS as err:
        print("User or password is not correct!", err)
    except:
        print("Unknown error!", sys.exc_info()[0])
    return False

class MyTestCase(unittest.TestCase):
    # ldap.INVALID_CREDENTIALS
    def test_something(self):
       print(isCheck())

if __name__ == '__main__':
    unittest.main()
