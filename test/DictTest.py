import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        d1 = {}
        d1.setdefault("k1","v1")
        d1.setdefault("k2","v2")
        d2 = {}
        d2.setdefault("k3","v3")
        d2.setdefault("k4","v4")
        #d3 = dict([d1,d2])
        d3 = {**d1,**d2}
        print(d3)


if __name__ == '__main__':
    unittest.main()
