from abc import abstractmethod

from Backened.filters.Filter import *


class TextFilter(Filter):
    def __init__(self, filter_name: str):
        self.type = "text"
        super().__init__(self.type, filter_name)


    @abstractmethod
    def filter(self, text_to_filter: str):
        pass