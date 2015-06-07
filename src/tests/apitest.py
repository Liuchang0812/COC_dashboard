import unittest
import sys
import json

sys.path.append("../core")
from api import *

class apitest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_clan_by_name(self):
        resp = clan_by_name('E7VMK')
	self.assertEquals('E7VMK7UK', resp["Name"])

if __name__ == '__main__':
    unittest.main()
