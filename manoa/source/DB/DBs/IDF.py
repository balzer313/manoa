import math

class IDF:
    def __init__(self, reverse_index_db, words_in_website):
        self.reverse_index_db = reverse_index_db
        self.words_in_website = words_in_website

    def get_word(self, word):
        return math.log(self.words_in_website/len(self.reverse_index_db[word]))
