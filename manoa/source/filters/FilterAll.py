from typing import List
from source.filters.Filter import Filter
from source.filters.ListFilter.Lemmatizer import Lemmatizer
from source.filters.ListFilter.Stopwords import Stopwords
from source.filters.TextFilter.Lower import Lower
from source.filters.TextFilter.Punctuation import Punctuation
from source.filters.TextFilter.Tokenaizer import Tokenaizer
from config.Log import logger



def filter_list_filters(filters, arg_to_filter):
    filtered = arg_to_filter

    for filter in filters:
        logger.info(f"Starting {filter.filter_name} filter...")
        filtered = filter.filter(filtered)
        logger.info(f"Finished {filter.filter_name} filter!")

    return filtered

def all_filters(text_to_filter: str, db):
    text_filter_list: List[Filter] = []
    text_filter_list.append(Lower())
    text_filter_list.append(Punctuation())
    text_filter_list.append(Tokenaizer())
    text_filtered_list = filter_list_filters(text_filter_list, text_to_filter)

    list_filter_list: List[Filter] = []
    list_filter_list.append(Stopwords(db))
    list_filter_list.append(Lemmatizer())
    list_filtered_list = filter_list_filters(list_filter_list, text_filtered_list)

    return list_filtered_list