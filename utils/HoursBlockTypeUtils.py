import re
import copy
from utils.DateUtils import DateUtils

class HoursBlockTypeUtils:
    @staticmethod
    def get_hours_block_type(hours_string):
        if HoursBlockTypeUtils.is_hours_string_single_day(hours_string):
            return 'singleDay'
        if HoursBlockTypeUtils.is_hours_string_single_group(hours_string):
            return 'singleGroup'
        if HoursBlockTypeUtils.is_hours_string_group_day_pre(hours_string):
            return 'groupDayPre'
        if HoursBlockTypeUtils.is_hours_string_group_day_post(hours_string):
            return 'groupDayPost'
        return False

    @staticmethod
    def is_hours_string_single_day(hours_string):
        return True if re.match("^[a-zA-Z]{3}\s[1-9]", hours_string) else False

    @staticmethod
    def is_hours_string_single_group(hours_string):
        return True if re.match("^[a-z]{3}-[a-z]{3}\s[1-9]", hours_string) else False

    @staticmethod
    def is_hours_string_group_day_pre(hours_string):
        return True if re.match("^[a-z]{3},\s[a-z]{3}-[a-z]{3}\s[1-9]", hours_string) else False

    @staticmethod
    def is_hours_string_group_day_post(hours_string):
        return True if re.match("^[a-z]{3}-[a-z]{3},\s[a-z]{3}\s[1-9]", hours_string) else False

    @staticmethod
    def group_hours_by_day(hours_blocks):
        days_of_week_dict = copy.deepcopy(DateUtils.days_of_week_dict)

        for hours_block in hours_blocks:
            if hours_block.get_type() == 'singleDay':
                day_string = hours_block.get_hours_block_string()[0:3]
                hour_string = hours_block.get_hours_block_string()[4:]

                days_of_week_dict[day_string].append(hour_string)
            elif hours_block.get_type() == 'singleGroup':
                start_day = hours_block.get_hours_block_string()[0:3]
                end_day = hours_block.get_hours_block_string()[4:7]
                hour_string = hours_block.get_hours_block_string()[8:]
                start_index = DateUtils.days_of_week_list.index(start_day)
                end_index = DateUtils.days_of_week_list.index(end_day)

                for i in range(start_index, end_index + 1):
                    days_of_week_dict[DateUtils.days_of_week_list[i]].append(hour_string)
            elif hours_block.get_type() == 'groupDayPre':
                single_day = hours_block.get_hours_block_string()[0:3]
                start_day = hours_block.get_hours_block_string()[5:8]
                end_day = hours_block.get_hours_block_string()[9:12]
                hour_string = hours_block.get_hours_block_string()[13:]
                start_index = DateUtils.days_of_week_list.index(start_day)
                end_index = DateUtils.days_of_week_list.index(end_day)

                days_of_week_dict[single_day].append(hour_string)
                for i in range(start_index, end_index + 1):
                    days_of_week_dict[DateUtils.days_of_week_list[i]].append(hour_string)
            elif hours_block.get_type() == 'groupDayPost':
                start_day = hours_block.get_hours_block_string()[0:3]
                end_day = hours_block.get_hours_block_string()[4:7]
                single_day = hours_block.get_hours_block_string()[9:12]
                hour_string = hours_block.get_hours_block_string()[13:]
                start_index = DateUtils.days_of_week_list.index(start_day)
                end_index = DateUtils.days_of_week_list.index(end_day)

                days_of_week_dict[single_day].append(hour_string)
                for i in range(start_index, end_index + 1):
                    days_of_week_dict[DateUtils.days_of_week_list[i]].append(hour_string)

        return days_of_week_dict
