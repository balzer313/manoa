
from abc import ABC, abstractmethod


class Filter(ABC):
    def __init__(self, filter_type, filter_name):
        self.filter_type = filter_type
        self.filter_name = filter_name
