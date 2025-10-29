from source.filters.ListFilter.Stopwords import *
from source.filters.FilterAll import *
from source.open import *


class Revi:
    def __init__(self, webs: List[str], db):
        self.db = db
        self.webs = webs

    def insert_web_words(self, inverted_index: dict[str, List[int]], website_words: List[str], website):
        for word in website_words:
            inverted_index.setdefault(word, {})[website] = [website_words.count(word), len(website_words)]

    def reverse_index(self):

        inverted_index: dict[str, List[int]] = {}
        files_path = self.db.get_configs()["paths"]["files_path"]
        read = self.db.get_configs()["file_settings"]["read"]

        for website in self.webs:
            website_content: str = read_file(f"{files_path}/{website}", read)
            website_words = all_filters(website_content, self.db)
            self.insert_web_words(inverted_index, website_words, website)

        return inverted_index