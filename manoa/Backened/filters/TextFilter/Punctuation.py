import re
import string
from Backened.filters.TextFilter.TextFilter import *


class Punctuation(TextFilter):
    def __init__(self):
        super().__init__("punctuation")

    def filter(self, text_to_filter: str):
        return re.sub('[%s]' % re.escape(string.punctuation), '', text_to_filter)