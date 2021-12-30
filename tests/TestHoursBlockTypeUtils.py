import unittest

from model.HoursBlockText import HoursBlockText
from utils.HoursBlockTypeUtils import HoursBlockTypeUtils

class TestStringutilsMethods(unittest.TestCase):
    def test_is_hours_string_single_day(self):
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("sun 11 am - 10 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("sun 11:00 am - 10 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("sun 11:00 am - 10:00 pm"), True)

        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("mon-sun 11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("mon-tue,sun  11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("sun, mon-tue  11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("sun, mon-tue  11:00 am - 10:00 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_day("sun, mon-tue  11 am - 10 pm"), False)

    def test_is_hours_string_single_group(self):
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("mon-sun 11 am - 10 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("mon-sun 11:00 am - 10 pm"), True)

        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("sun 11:00 am - 10:00 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("mon-tue,sun  11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("sun, mon-tue  11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("sun, mon-tue  11:00 am - 10:00 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_single_group("sun, mon-tue  11 am - 10 pm"), False)

    def test_is_hours_string_group_day_pre(self):
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("sun, mon-tue 11:00 am - 10 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("sun, mon-tue 11:00 am - 10:00 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("sun, mon-tue 11 am - 10 pm"), True)

        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("mon-sun 11 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("mon-sun 11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("sun 11:00 am - 10:00 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_pre("mon-tue,sun  11:00 am - 10 pm"), False)

    def test_is_hours_string_group_day_post(self):
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-tue, sun 11:00 am - 10 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-tue, wed 11 am - 10 pm"), True)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-tue, sun 11:00 am - 10:30 pm"), True)

        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-tue,sun 11:00 am - 10:30 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-tue,sun 11:00 am-10:30 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("sun, mon-tue 11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("sun, mon-tue 11:00 am - 10:00 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("sun, mon-tue 11 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-sun 11 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("mon-sun 11:00 am - 10 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.is_hours_string_group_day_post("sun 11:00 am - 10:00 pm"), False)

    def test_get_hours_block_type(self):
        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type("mon-tue, sun 11:00 am - 10:30 pm"), "groupDayPost")
        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type("sun, mon-tue 11:00 am - 10:30 pm"), "groupDayPre")
        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type("sun 11:00 am - 10:30 pm"), "singleDay")
        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type("mon-wed 11:00 am - 10:30 pm"), "singleGroup")

        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type("123-wed 11:00 am - 10:30 pm"), False)
        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type(""), False)
        self.assertEqual(HoursBlockTypeUtils.get_hours_block_type("mon-wed, tue-thu 11:00am - 6:00pm"), False)

    def test_group_hours_by_day(self):
        hours_blocks = [HoursBlockText("mon-sun 11:00 am - 10 pm")]
        hours_blocks_by_day = HoursBlockTypeUtils.group_hours_by_day(hours_blocks)
        correct_response = {
            "mon": ["11:00 am - 10 pm"],
            "tue": ["11:00 am - 10 pm"],
            "wed": ["11:00 am - 10 pm"],
            "thu": ["11:00 am - 10 pm"],
            "fri": ["11:00 am - 10 pm"],
            "sat": ["11:00 am - 10 pm"],
            "sun": ["11:00 am - 10 pm"],
        }
        self.assertEqual(hours_blocks_by_day, correct_response)

        hours_blocks = [HoursBlockText("mon-thu 11 am - 11 pm")]
        hours_blocks_by_day = HoursBlockTypeUtils.group_hours_by_day(hours_blocks)
        correct_response = {
            "mon": ["11 am - 11 pm"],
            "tue": ["11 am - 11 pm"],
            "wed": ["11 am - 11 pm"],
            "thu": ["11 am - 11 pm"],
            "fri": [],
            "sat": [],
            "sun": [],
        }
        self.assertEqual(hours_blocks_by_day, correct_response)

        hours_blocks = [HoursBlockText("sun 10 am - 11 pm")]
        hours_blocks_by_day = HoursBlockTypeUtils.group_hours_by_day(hours_blocks)
        correct_response = {
            "mon": [],
            "tue": [],
            "wed": [],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": ["10 am - 11 pm"],
        }
        self.assertEqual(hours_blocks_by_day, correct_response)

        hours_blocks = [HoursBlockText("mon-wed, sun 10 am - 11 pm")]
        hours_blocks_by_day = HoursBlockTypeUtils.group_hours_by_day(hours_blocks)
        correct_response = {
            "mon": ["10 am - 11 pm"],
            "tue": ["10 am - 11 pm"],
            "wed": ["10 am - 11 pm"],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": ["10 am - 11 pm"],
        }
        self.assertEqual(hours_blocks_by_day, correct_response)

        hours_blocks = [HoursBlockText("sun, mon-wed 10 am - 11 pm")]
        hours_blocks_by_day = HoursBlockTypeUtils.group_hours_by_day(hours_blocks)
        correct_response = {
            "mon": ["10 am - 11 pm"],
            "tue": ["10 am - 11 pm"],
            "wed": ["10 am - 11 pm"],
            "thu": [],
            "fri": [],
            "sat": [],
            "sun": ["10 am - 11 pm"],
        }
        self.assertEqual(hours_blocks_by_day, correct_response)

if __name__ == '__main__':
    unittest.main()
