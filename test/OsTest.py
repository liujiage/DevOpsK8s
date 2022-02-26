import unittest
import os

from services.ParseService import getServices
from vo.ServiceVO import ServiceVO

class MyTestCase(unittest.TestCase):
    def test_files(self):
        f = []
        pathName = r'/Users/liujiage/tmp/hosts'
        for root, dirs, files in os.walk(pathName):
            for file in files:
                # .hosts file only
                if not file.endswith('.hosts'):
                    continue
                file_path = os.path.join(root, file)
                f.append(file_path)
            # parents folder level 1 only
            break
        print(f)

    def test_pares_file(self):
        f = r'/Users/liujiage/tmp/hosts/tiny.hosts'
        getServices(f)

    def test_file_type(self):
        fileName = "./content.hosts"
        print(fileName.endswith(".hosts"))



if __name__ == '__main__':
    unittest.main()
