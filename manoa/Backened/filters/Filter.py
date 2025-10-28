
from abc import ABC
from Fronted.logs.Log import logger


class Filter(ABC):
    def __init__(self, filter_type, filter_name):
        self.filter_type = filter_type
        self.filter_name = filter_name


    @staticmethod
    def filter_list_filters(filters, arg_to_filter):
        filtered = arg_to_filter
        for filter in filters:
            logger.info(f"Starting {filter.filter_name} filter...")
            filtered = filter.filter(filtered)
            logger.info(f"Finished {filter.filter_name} filter!")
        return filtered