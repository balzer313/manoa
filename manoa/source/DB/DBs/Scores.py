from typing import List

class Scores:
    def __init__(self, engine):
        self.engine = engine
        self.revi_db = self.engine.db.get_revi()

    def create_web_scores(self, word: str):
        for web in self.revi_db[word]:
            self.scores.setdefault(word, {})[web] = {self.engine.get_tf_idf(word, web)}

    def create_scores(self):
        self.scores: dict[str, List] = {}

        for word in self.revi_db:
            self.create_web_scores(word)

        return self.scores