from utils.HoursUtils import HoursUtils
from model.HoursBlockText import HoursBlockText
from utils.HoursBlockTypeUtils import HoursBlockTypeUtils

class Restaurant:
    def __init__(self, name, raw_hours_string):
        self.name = name
        self.raw_hours_string = raw_hours_string
        self.raw_hours_list = HoursUtils.hours_string_to_list(raw_hours_string)

        self.hours_blocks = []
        for hours_string in self.raw_hours_list:
            self.hours_blocks.append(HoursBlockText(hours_string))

        # TODO: Move group_hours_by_day to hours utils
        self.daily_hours = HoursBlockTypeUtils.group_hours_by_day(self.hours_blocks)
        self.daily_hours = HoursUtils.convert_to_military_time(self.daily_hours)
        self.daily_hours = HoursUtils.split_times_crossing_midnight(self.daily_hours)

    def get_name(self):
        return self.name

    def get_raw_hours_string(self):
        return self.raw_hours_string

    def get_raw_hours_list(self):
        return self.raw_hours_list

    def get_hours_blocks(self):
        return self.hours_blocks

    def get_daily_hours(self):
        return self.daily_hours
