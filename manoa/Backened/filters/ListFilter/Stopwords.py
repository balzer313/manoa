from Backened.filters.ListFilter.ListFilter import *

class Stopwords(ListFilter):
    def __init__(self, db):
        super().__init__("stopwords")
        self.db = db

    def filter(self, word_list: List[str]):
        return list(filter(self.word_in_stopwords, word_list))

    def word_in_stopwords(self, word: str):
        content = self.db.get_stopwords()
        if word in content: return False
        else: return True