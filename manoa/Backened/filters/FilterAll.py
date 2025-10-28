from typing import List

from Backened.filters.Filter import Filter
from Backened.filters.ListFilter.Lemmatizer import Lemmatizer
from Backened.filters.ListFilter.ListFilter import ListFilter
from Backened.filters.ListFilter.Stopwords import Stopwords
from Backened.filters.TextFilter.Lower import Lower
from Backened.filters.TextFilter.Punctuation import Punctuation
from Backened.filters.TextFilter.TextFilter import TextFilter
from Backened.filters.TextFilter.Tokenaizer import Tokenaizer


class FilterAll:
    @staticmethod
    def all_filters(text_to_filter: str, db):
        text_filter_list: List[Filter] = []
        text_filter_list.append(Lower())
        text_filter_list.append(Punctuation())
        text_filter_list.append(Tokenaizer())
        text_filtered_list = TextFilter.filter_list_filters(text_filter_list, text_to_filter)
        list_filter_list: List[Filter] = []
        list_filter_list.append(Stopwords(db))
        list_filter_list.append(Lemmatizer())
        list_filtered_list = ListFilter.filter_list_filters(list_filter_list, text_filtered_list)
        return list_filtered_list