import unittest

from utils.StringUtils import StringUtils

class TestStringutilsMethods(unittest.TestCase):
    def test_normalize_string(self):
        self.assertEqual(StringUtils.normalize_string("Mon-Sun 11:00 am - 10 pm"), "mon-sun 11:00 am - 10 pm")
        self.assertEqual(StringUtils.normalize_string("Mon-Tues 11:00 am - 10 pm"), "mon-tue 11:00 am - 10 pm")
        self.assertEqual(StringUtils.normalize_string("MoN-SUN       11:00  Am  -  10  pM"), "mon-sun 11:00 am - 10 pm")
        self.assertEqual(StringUtils.normalize_string("   Mon-Sun 11:00 am - 10 pm    "), "mon-sun 11:00 am - 10 pm")
        self.assertEqual(StringUtils.normalize_string("TUES 11  am -  10 pm "), "tue 11 am - 10 pm")

if __name__ == '__main__':
    unittest.main()
