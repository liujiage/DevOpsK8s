import unittest
class MyTestCase(unittest.TestCase):
    def test_dic(self):
        di = {}
        di.setdefault("id",1)
        di.setdefault("name","jiage")
        print(di.get("id"))
        print(di.get("name"))

if __name__ == '__main__':
    unittest.main()
