class HoursOfOperation:
    def __init__(self, open_military_time, close_military_time):
        self.open_military_time = open_military_time
        self.close_military_time = close_military_time

    def get_close_time(self):
        return self.close_military_time

    def get_open_time(self):
        return self.open_military_time
