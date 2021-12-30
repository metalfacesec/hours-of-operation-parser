class DateUtils:
    days_of_week_list = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    days_of_week_dict = {
        'mon': [],
        'tue': [],
        'wed': [],
        'thu': [],
        'fri': [],
        'sat': [],
        'sun': []
    }

    @staticmethod
    def get_next_day_of_week(day):
        day_index = DateUtils.days_of_week_list.index(day)
        next_day_index = day_index + 1

        if day_index == len(DateUtils.days_of_week_list) - 1:
            next_day_index = 0

        return DateUtils.days_of_week_list[next_day_index]
