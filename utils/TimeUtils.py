from datetime import datetime

class TimeUtils:
    @staticmethod
    def get_time_format(time_string):
        time_format = '%I'
        if ':' in time_string:
            time_format += ":%M"
        time_format += " %p"
        return time_format

    @staticmethod
    def regular_to_military(time_string):
        time = datetime.strptime(time_string, TimeUtils.get_time_format(time_string))
        return datetime.strftime(time, "%H:%M")

    @staticmethod
    def do_hours_cross_midnight(open_time, close_time):
        if close_time == "00:00":
            return False

        open = int(open_time.split(':')[0])
        close = int(close_time.split(':')[0])

        return close < open
