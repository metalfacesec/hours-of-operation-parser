import re

class StringUtils:
    @staticmethod
    def normalize_string(hoursString):
        # Lowercase everything and string whitespace from start and end of string
        hoursString = hoursString.strip().lower()

        # Replace tues with tue so all days use 3 letters making our regex a little cleaner
        hoursString = hoursString.replace('tues', 'tue')

        # Replace all instances of more than one space together with a single space
        return re.sub('\s+', ' ', hoursString)