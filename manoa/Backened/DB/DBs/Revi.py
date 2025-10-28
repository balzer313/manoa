from Backened.filters.ListFilter.Stopwords import *
from Backened.filters.FilterAll import FilterAll
from FileInfos.config.configs import Config


class Revi:
    def __init__(self, webs: List[str], db):
        self.db = db
        self.webs = webs


    def reverse_index(self):
        inverted_index: dict[str, List[int]] = {}
        files_path = Config.load_config()["paths"]["files_path"]
        for website in self.webs:
            with open(f"{files_path}/{website}", 'r') as f:
                website_content: str = f.read()
                website_words = FilterAll.all_filters(website_content, self.db)
                for word in website_words:
                    inverted_index.setdefault(word, {})[website] = [website_words.count(word), len(website_words)]
        return inverted_index