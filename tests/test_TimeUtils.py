import unittest

from utils.TimeUtils import TimeUtils

class TestTimeUtilsMethods(unittest.TestCase):
    def test_get_time_format(self):
        self.assertEqual(TimeUtils.get_time_format("11:00 am"), "%I:%M %p")
        self.assertEqual(TimeUtils.get_time_format("11 am"), "%I %p")
        self.assertEqual(TimeUtils.get_time_format("01 am"), "%I %p")
        self.assertEqual(TimeUtils.get_time_format("1 am"), "%I %p")
        self.assertEqual(TimeUtils.get_time_format("01:15 am"), "%I:%M %p")
        self.assertEqual(TimeUtils.get_time_format("1:15 am"), "%I:%M %p")

    def test_regular_to_military(self):
        self.assertEqual(TimeUtils.regular_to_military("11:00 am"), "11:00")
        self.assertEqual(TimeUtils.regular_to_military("11 am"), "11:00")
        self.assertEqual(TimeUtils.regular_to_military("11:00 pm"), "23:00")
        self.assertEqual(TimeUtils.regular_to_military("11 pm"), "23:00")
        self.assertEqual(TimeUtils.regular_to_military("12 pm"), "12:00")
        self.assertEqual(TimeUtils.regular_to_military("12:00 pm"), "12:00")
        self.assertEqual(TimeUtils.regular_to_military("12 am"), "00:00")
        self.assertEqual(TimeUtils.regular_to_military("12:00 am"), "00:00")
        self.assertEqual(TimeUtils.regular_to_military("1 am"), "01:00")
        self.assertEqual(TimeUtils.regular_to_military("1 pm"), "13:00")
        self.assertEqual(TimeUtils.regular_to_military("1:00 am"), "01:00")
        self.assertEqual(TimeUtils.regular_to_military("1:00 pm"), "13:00")

    def test_do_hours_cross_midnight(self):
        self.assertEqual(TimeUtils.do_hours_cross_midnight("11:00", "12:00"), False)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("2:00", "12:00"), False)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("02:00", "12:00"), False)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("02:00", "15:00"), False)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("06:00", "00:00"), False)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("12:00", "00:00"), False)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("13:00", "00:00"), False)

        self.assertEqual(TimeUtils.do_hours_cross_midnight("13:00", "00:01"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("05:00", "00:31"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("22:00", "01:01"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("12:00", "2:00"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("12:00", "02:00"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("6:00", "04:00"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("06:00", "04:00"), True)
        self.assertEqual(TimeUtils.do_hours_cross_midnight("6:00", "4:00"), True)

if __name__ == '__main__':
    unittest.main()
