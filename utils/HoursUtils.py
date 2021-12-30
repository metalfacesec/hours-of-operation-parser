import copy
from utils.DateUtils import DateUtils
from utils.TimeUtils import TimeUtils
from utils.StringUtils import StringUtils
from model.HoursOfOperation import HoursOfOperation

class HoursUtils:
    @staticmethod
    def hours_string_to_list(hours_string):
        return list(map(StringUtils.normalize_string, hours_string.split(' / ')))

    @staticmethod
    def convert_to_military_time(hours):
        military_time_hours = {}
        for day, hours in hours.items():
            military_time_hours[day] = []
            for hour_string in hours:
                open_time = TimeUtils.regular_to_military(hour_string.split(' - ')[0])
                close_time = TimeUtils.regular_to_military(hour_string.split(' - ')[1])
                store_hours = HoursOfOperation(open_time, close_time)
                military_time_hours[day].append(store_hours)

        return military_time_hours

    @staticmethod
    def split_times_crossing_midnight(hours):
        split_hours = copy.deepcopy(hours)

        for day, hours_of_operation in split_hours.items():
            for operating_hours in hours_of_operation:
                if TimeUtils.do_hours_cross_midnight(operating_hours.get_open_time(), operating_hours.get_close_time()):
                    next_day = DateUtils.get_next_day_of_week(day)

                    split_hours[next_day].append(HoursOfOperation('00:00', operating_hours.get_close_time()))

                    split_hours[day].pop(0)
                    split_hours[day].append(HoursOfOperation(operating_hours.get_open_time(), "00:00"))

        return split_hours

    @staticmethod
    def is_restaurant_open(restaurant_hours, day_of_week, time):
        if not len(restaurant_hours[day_of_week]):
            return False

        time_int = int(time.replace(":", ""))

        daily_hours = restaurant_hours[day_of_week]
        for hours in daily_hours:
            open_int = int(hours.get_open_time().replace(":", ""))
            close_int = int(hours.get_close_time().replace(":", ""))

            if time_int == 0 and close_int == 0:
                return True

            if time_int > open_int and close_int == 0:
                return True

            if time_int >= open_int and time_int <= close_int:
                return True

        return False
