import unittest

from utils.HoursUtils import HoursUtils
from model.HoursOfOperation import HoursOfOperation

class TestHoursUtilsMethods(unittest.TestCase):
    def test_is_restaurant_open(self):
        hours = {
            "mon": [],
            "tue": [HoursOfOperation("12:00", "22:00")],
            "wed": [HoursOfOperation("12:00", "22:00")],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": []
        }

        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "12:00"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "12:05"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "22:00"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "21:59"), True)

        self.assertEqual(HoursUtils.is_restaurant_open(hours, "mon", "01:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "thu", "01:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "fri", "01:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "sat", "01:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "sun", "01:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "11:00"), False)

        hours = {
            "mon": [HoursOfOperation("00:00", "01:00")],
            "tue": [HoursOfOperation("12:00", "22:00")],
            "wed": [HoursOfOperation("12:00", "22:00")],
            "thu": [HoursOfOperation("13:00", "00:00")],
            "fri": [HoursOfOperation("00:00", "01:30"), HoursOfOperation("13:00", "00:00")],
            "sat": [HoursOfOperation("00:00", "02:00"), HoursOfOperation("13:00", "00:00")],
            "sun": [HoursOfOperation("00:00", "02:00"), HoursOfOperation("13:00", "00:00")]
        }
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "mon", "01:00"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "mon", "00:30"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "12:00"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "14:30"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "22:00"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "wed", "12:35"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "wed", "22:00"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "thu", "13:35"), True)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "thu", "00:00"), True)

        self.assertEqual(HoursUtils.is_restaurant_open(hours, "mon", "11:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "23:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "tue", "11:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "thu", "11:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "fri", "02:00"), False)
        self.assertEqual(HoursUtils.is_restaurant_open(hours, "fri", "11:00"), False)

    def test_convert_to_military_time(self):
        hours = {
            "mon": ["10 am - 11 pm"],
            "tue": ["11 am - 11 pm"],
            "wed": ["12:30 pm - 2 am"],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": ["10 am - 11 pm"],
        }
        military_hours_correct = {
            "mon": [HoursOfOperation("10:00", "23:00")],
            "tue": [HoursOfOperation("11:00", "23:00")],
            "wed": [HoursOfOperation("12:30", "02:00")],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": [HoursOfOperation("10:00", "23:00")],
        }

        converted_times = HoursUtils.convert_to_military_time(hours)
        for day, values in converted_times.items():
            if not len(converted_times[day]):
                continue
            for idx, val in enumerate(converted_times[day]):
                self.assertEqual(converted_times[day][idx].get_open_time(), military_hours_correct[day][idx].get_open_time())
                self.assertEqual(converted_times[day][idx].get_close_time(), military_hours_correct[day][idx].get_close_time())

        hours = {
            "mon": ["6 am - 11 pm"],
            "tue": ["11 am - 12 pm"],
            "wed": ["12:30 pm - 2 am"],
            "thu": ["9 am - 10 pm"],
            "fri": ["03 pm - 02 am"],
            "sat": [],
            "sun": ["10 am - 11 pm"],
        }
        military_hours_correct = {
            "mon": [HoursOfOperation("06:00", "23:00")],
            "tue": [HoursOfOperation("11:00", "12:00")],
            "wed": [HoursOfOperation("12:30", "02:00")],
            "thu": [HoursOfOperation("09:00", "22:00")],
            "fri": [HoursOfOperation("15:00", "02:00")],
            "sat": [],
            "sun": [HoursOfOperation("10:00", "23:00")],
        }
        converted_times = HoursUtils.convert_to_military_time(hours)
        for day, values in converted_times.items():
            if not len(converted_times[day]):
                continue
            for idx, val in enumerate(converted_times[day]):
                self.assertEqual(converted_times[day][idx].get_open_time(),
                                 military_hours_correct[day][idx].get_open_time())
                self.assertEqual(converted_times[day][idx].get_close_time(),
                                 military_hours_correct[day][idx].get_close_time())

    def test_hours_string_to_list(self):
        result = ["mon-sun 11:00 am - 10 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Sun 11:00 am - 10 pm"), result)

        result = ["mon-sun 11 am - 9:30 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Sun 11 am - 9:30 pm"), result)

        result = ["mon-fri, sat 11 am - 12 pm", "sun 11 am - 10 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Fri, Sat 11 am - 12 pm  / Sun 11 am - 10 pm"), result)

        result = ["tue-fri, sun 11:30 am - 10 pm", "sat 5:30 pm - 11 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Tues-Fri, Sun 11:30 am - 10 pm  / Sat 5:30 pm - 11 pm"), result)

        result = ["mon-thu 11 am - 11 pm", "fri-sat 11 am - 12:30 am", "sun 10 am - 11 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Thu 11 am - 11 pm  / Fri-Sat 11 am - 12:30 am  / Sun 10 am - 11 pm"), result)

        result = ["mon-thu 11:30 am - 10 pm", "fri-sun 11:30 am - 11 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Thu 11:30 am - 10 pm  / Fri-Sun 11:30 am - 11 pm"), result)

        result = ["mon-wed 5 pm - 12:30 am", "thu-fri 5 pm - 1:30 am", "sat 3 pm - 1:30 am", "sun 3 pm - 11:30 pm"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Wed 5 pm - 12:30 am  / Thu-Fri 5 pm - 1:30 am  / Sat 3 pm - 1:30 am  / Sun 3 pm - 11:30 pm"), result)

        result = ["mon-thu, sun 11 am - 10 pm", "fri-sat 11 am - 12 am"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Thu, Sun 11 am - 10 pm  / Fri-Sat 11 am - 12 am"), result)

        result = ["mon-sat 11 am - 12 am", "sun 12 pm - 2 am"]
        self.assertEqual(HoursUtils.hours_string_to_list("mon-sat 11 am - 12 am  / sun 12 pm - 2 am"), result)

        result = ["mon-sun 11 am - 4 am"]
        self.assertEqual(HoursUtils.hours_string_to_list("Mon-Sun 11 am - 4 am"), result)

    def test_split_times_crossing_midnight(self):
        hours = {
            "mon": [HoursOfOperation("13:00", "02:00")],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": [],
        }
        result = {
            "mon": [HoursOfOperation("13:00", "00:00")],
            "tue": [HoursOfOperation("00:00", "02:00")],
            "wed": [],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": [],
        }
        converted_times = HoursUtils.split_times_crossing_midnight(hours)
        for day, values in converted_times.items():
            if not len(converted_times[day]):
                continue
            for idx, val in enumerate(converted_times[day]):
                self.assertEqual(converted_times[day][idx].get_open_time(), result[day][idx].get_open_time())
                self.assertEqual(converted_times[day][idx].get_close_time(), result[day][idx].get_close_time())

        hours = {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": [HoursOfOperation("13:00", "02:00")]
        }
        result = {
            "mon": [HoursOfOperation("00:00", "02:00")],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": [HoursOfOperation("13:00", "00:00")]
        }
        converted_times = HoursUtils.split_times_crossing_midnight(hours)
        for day, values in converted_times.items():
            if not len(converted_times[day]):
                continue
            for idx, val in enumerate(converted_times[day]):
                self.assertEqual(converted_times[day][idx].get_open_time(), result[day][idx].get_open_time())
                self.assertEqual(converted_times[day][idx].get_close_time(), result[day][idx].get_close_time())

        hours = {
            "mon": [],
            "tue": [HoursOfOperation("12:00", "22:00")],
            "wed": [HoursOfOperation("12:00", "22:00")],
            "thu": [HoursOfOperation("13:00", "01:30")],
            "fri": [HoursOfOperation("13:00", "02:00")],
            "sat": [HoursOfOperation("13:00", "02:00")],
            "sun": [HoursOfOperation("13:00", "01:00")]
        }
        result = {
            "mon": [HoursOfOperation("00:00", "01:00")],
            "tue": [HoursOfOperation("12:00", "22:00")],
            "wed": [HoursOfOperation("12:00", "22:00")],
            "thu": [HoursOfOperation("13:00", "00:00")],
            "fri": [HoursOfOperation("00:00", "01:30"), HoursOfOperation("13:00", "00:00")],
            "sat": [HoursOfOperation("00:00", "02:00"), HoursOfOperation("13:00", "00:00")],
            "sun": [HoursOfOperation("00:00", "02:00"), HoursOfOperation("13:00", "00:00")]
        }
        converted_times = HoursUtils.split_times_crossing_midnight(hours)
        for day, values in converted_times.items():
            if not len(converted_times[day]):
                continue
            for idx, val in enumerate(converted_times[day]):
                self.assertEqual(converted_times[day][idx].get_open_time(), result[day][idx].get_open_time())
                self.assertEqual(converted_times[day][idx].get_close_time(), result[day][idx].get_close_time())

if __name__ == '__main__':
    unittest.main()
