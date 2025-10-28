from abc import abstractmethod
from typing import List

from Backened.filters.Filter import *


class ListFilter(Filter):
    def __init__(self, filter_name: str):
        self.type = "list"
        super().__init__(self.type, filter_name)

    @abstractmethod
    def filter(self, list_to_filter: List):
        pass