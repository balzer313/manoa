

class TF:
    def __init__(self, revi_db):
        self.revi_db = revi_db

    def get_word(self, word, web):
        revi_word = self.revi_db[word]
        return 0 if web not in revi_word.keys() else revi_word[web][0]/revi_word[web][1]