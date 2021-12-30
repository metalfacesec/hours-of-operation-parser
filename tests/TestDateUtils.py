import unittest

from utils.DateUtils import DateUtils

class TestDateUtilsMethods(unittest.TestCase):
    def test_get_next_day_of_week(self):
        self.assertEqual(DateUtils.get_next_day_of_week('mon'), 'tue')
        self.assertEqual(DateUtils.get_next_day_of_week('tue'), 'wed')
        self.assertEqual(DateUtils.get_next_day_of_week('wed'), 'thu')
        self.assertEqual(DateUtils.get_next_day_of_week('thu'), 'fri')
        self.assertEqual(DateUtils.get_next_day_of_week('fri'), 'sat')
        self.assertEqual(DateUtils.get_next_day_of_week('sat'), 'sun')
        self.assertEqual(DateUtils.get_next_day_of_week('sun'), 'mon')

if __name__ == '__main__':
    unittest.main()