import unittest
from collections import OrderedDict


class MyTestCase(unittest.TestCase):
    def test_something(self):
        d = {"account": 'z', "tiny": 'y', "admin.api": 'x', "NS": 'n'}
        r = {}
        ks = [key for key in d]
        print(ks)
        print(ks.sort(key=str.lower))
        print(ks)
        for k in ks:
            r.setdefault(k, d.get(k))
        print(r)

if __name__ == '__main__':
    unittest.main()
