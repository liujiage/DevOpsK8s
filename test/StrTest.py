import os
import string
import unittest

from common.StrUtils import isEmpty, isAnyEmpty
from vo.LogVO import LogVO


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # ./deploy-web.sh account 397 dp 10.30.0.48,10.30.0.49 1
        n = "dp"
        c = "./deploy-web.sh"
        p = "version-100,tiny-192.168.1.0,tiny-192.168.1.2,tiny-##192.168.1.3"
        ps = p.split(",")
        v, s, ip = "", "", ""
        v = ps[0].split("-")[1]
        s = ps[1].split("-")[0]
        ip = p.replace(ps[0]+",","").replace(s+"-","").replace("#","")
        r = "{0} {1} {2} {3} {4}".format(c,s,v,n,ip)
        print("{0}".format(r))

    def test_empty(self):
        s = []
        print(type(s) is list)
        print(isEmpty(s))

    def test_any_empty(self):
        print(isAnyEmpty(["111","1111","ccc","2222",LogVO()]))

    def test_get_path(self):
        print(os.path.abspath(os.curdir))
        print(os.path.abspath(os.pardir))

    def test_str_path(self):
        c = "/liujiage/histroy"
        id = "xxxxid"
        print("cat {0}/{1}".format(c, id))

    def test_num(self):
        n = round(70 / 50)
        print(n)




if __name__ == '__main__':
    unittest.main()
