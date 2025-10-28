from typing import List

class Scores:
    def __init__(self, engine):
        self.engine = engine
        self.revi_db = self.engine.db.get_revi()

    def create_scores(self):
        scores: dict[str, List] = {}
        for word in self.revi_db:
            for web in self.revi_db[word]:
                scores.setdefault(word, {})[web] = {self.engine.get_tf_idf(word, web)}
        return scores