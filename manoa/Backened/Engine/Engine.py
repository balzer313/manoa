from typing import Callable, List
from Backened.DB.DB import DB
from Backened.DB.DBs.IDF import IDF
from Backened.DB.DBs.Revi import Revi
from Backened.DB.DBs.Scores import Scores
from Backened.DB.DBs.TF import TF
from Backened.Engine.Websites import Websites
from Backened.filters.FilterAll import FilterAll
from FileInfos.config.configs import Config
from Fronted.logs.Log import logger



class Engine:
    def __init__(self):
        logger.debug("Engine is on")
        self.config = Config.load_config()
        self.websites = Websites(self.config["paths"]["files_path"]).get_websites()
        self.db = DB()
        self.create_dbs()
    def create_dbs(self):
        logger.info("Creating dbs...")
        create_db_list: List[Callable] = []
        create_db_list.append(self.create_stopwords_db)
        create_db_list.append(self.create_revi_db)
        create_db_list.append(self.create_tf_db)
        create_db_list.append(self.create_idf_db)
        create_db_list.append(self.create_scores_db)
        for function in create_db_list:
            logger.info(f"Starting to create db with: {function.__name__}...")
            function()
            logger.info(f"Finished creating db with: {function.__name__}!")
        logger.info("Finished creating dbs!")

    def create_revi_db(self):
        revi = Revi(self.websites, self.db).reverse_index()
        self.db.set_revi(revi)

    def create_tf_db(self):
        tf = TF(self.db.get_revi())
        self.db.set_tf(tf)

    def create_idf_db(self):
        idf = IDF(self.db.get_revi(), len(self.websites))
        self.db.set_idf(idf)

    def create_scores_db(self):
        scores = Scores(self).create_scores()
        self.db.set_scores(scores)

    def create_stopwords_db(self):
        stopwords_path = Config.load_config()["paths"]["stopwords_path"]
        with open(stopwords_path, "r") as file:
            self.db.set_stopwords(file.read())

    def get_tf_idf(self, word, web):
        if self.db.get_tf() is None or self.db.get_idf() is None: return None
        return self.db.get_tf().get_word(word, web) * self.db.get_idf().get_word(word)

    def filter_query_list(self, query):
        logger.info(f"Filtering the query: '{query}'...")
        filtered_list = FilterAll.all_filters(query, self.db)
        logger.info(f"Finished filtering: '{filtered_list}'")
        return filtered_list



    def searching(self, query: str):
        try:
            logger.info(f"Starts searching for '{query}'")
            query_list = self.filter_query_list(query)
            scorings: dict[str, float] = {}
            for word in query_list:
                logger.info(f"Searching for word '{word}'")
                for web in self.db.get_scores()[word]:
                    if web not in scorings:
                        scorings[web] = self.db.get_scores()[word][web]
                    else:
                        scorings[web] = scorings[web] + self.db.get_scores()[word][web]
            results = sorted(scorings.items(), key=lambda item: item[1], reverse=True)[:3]
            logger.info(f"Found results: {results}")
            return results
        except Exception as error:
            logger.error(error)
            return error


    def print_results(self, results: List[set]):
        try:
            if len(results) > 3: return None
            for i in range(len(results)):
                print(f"{i + 1}s place: {results[i][0]}, with accuracy of {results[i][1]}")
        except Exception as error:
            logger.error(error)
            print(f"Error")
