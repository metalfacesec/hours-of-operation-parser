from utils.HoursBlockTypeUtils import HoursBlockTypeUtils

class HoursBlockText:
    def __init__(self, hours_block_string):
        self.hours_block_string = hours_block_string
        self.type = HoursBlockTypeUtils.get_hours_block_type(hours_block_string)

    def get_hours_block_string(self):
        return self.hours_block_string

    def get_type(self):
        return self.type
