from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from Backened.filters.ListFilter.ListFilter import *


class Lemmatizer(ListFilter):
    def __init__(self):
        super().__init__("lemmatizer")
        self.lemmatizer = WordNetLemmatizer()

    def get_wordnet_pos(self, tag):
        if tag.startswith('J'):
            return 'a'
        elif tag.startswith('V'):
            return 'v'
        elif tag.startswith('N'):
            return 'n'
        elif tag.startswith('R'):
            return 'r'
        else:
            return 'n'

    def filter(self, list_to_filter: List):
        tagged_tokens = pos_tag(list_to_filter)
        lemmatized_sentence = []
        for word, tag in tagged_tokens:
            if word.endswith("ing"): lemmatized_sentence.append(word[:-3])
            else: lemmatized_sentence.append(self.lemmatizer.lemmatize(word, self.get_wordnet_pos(tag)))
        return lemmatized_sentence

