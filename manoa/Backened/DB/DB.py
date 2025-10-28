from Backened.DB.DBs.Scores import *

class DB:
    def __init__(self):
        self.revi_db = None
        self.tf_db = None
        self.idf_db = None
        self.scores = None
        self.stopwords: List[str] = None

    def get_revi(self): return self.revi_db

    def get_tf(self): return self.tf_db

    def get_idf(self): return self.idf_db

    def get_scores(self): return self.scores

    def get_stopwords(self): return self.stopwords

    def set_revi(self, reverse_index): self.revi_db = reverse_index

    def set_tf(self, tf): self.tf_db = tf

    def set_idf(self, idf): self.idf_db = idf

    def set_scores(self, scores): self.scores = scores

    def set_stopwords(self, stopwords): self.stopwords = stopwords
