from abc import abstractmethod
from typing import List
from config.Log import logger
from source.filters.Filter import *


class ListFilter(Filter):
    def __init__(self, filter_name: str):
        self.type = "list"
        super().__init__(self.type, filter_name)

    @abstractmethod
    def filter(self, text_to_filter: str):
        error_message: str = "filter function is missing"
        logger.error(error_message)
        raise Exception(error_message)