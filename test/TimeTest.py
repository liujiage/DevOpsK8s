import unittest
from datetime import datetime, timezone

class MyTestCase(unittest.TestCase):
    def test_something(self):
        now_utc = datetime.now(timezone.utc)
        print(now_utc.strftime('%Y%m%d%H%M%S'))


if __name__ == '__main__':
    unittest.main()
