from Backened.filters.TextFilter.TextFilter import *


class Tokenaizer(TextFilter):
    def __init__(self):
        super().__init__("tokenaizer")

    def filter(self, text_to_filter: str):
        return text_to_filter.split()
