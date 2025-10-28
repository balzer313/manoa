from Backened.filters.TextFilter.TextFilter import *


class Lower(TextFilter):
    def __init__(self):
        super().__init__("lower")

    def filter(self, text_to_filter: str):
        return text_to_filter.lower()