from typing import Callable, List
from source.DB.DB import DB
from source.DB.DBs.IDF import IDF
from source.DB.DBs.Revi import Revi
from source.DB.DBs.Scores import Scores
from source.DB.DBs.TF import TF
from source.Engine.Websites import Websites
from source.filters.FilterAll import *
from config.configs import *
from config.Log import logger
from source.open import *



class Engine:
    def __init__(self):
        logger.debug("Engine is on")
        self.config = load_config()
        self.websites = Websites(self.config["paths"]["files_path"]).get_websites()
        self.db = DB()
        self.create_dbs()
    def create_dbs(self):
        logger.info("Creating dbs...")
        create_db_list: List[Callable] = []
        create_db_list.append(self.create_configs_db)
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
        stopwords_path = self.db.get_configs()["paths"]["stopwords_path"]
        read = self.db.get_configs()["file_settings"]["read"]
        content: str = read_file(stopwords_path, read)
        self.db.set_stopwords(content)

    def create_configs_db(self):
        self.db.set_configs(self.config)

    def get_tf_idf(self, word, web):
        if self.db.get_tf() is None or self.db.get_idf() is None: return None
        return self.db.get_tf().get_word(word, web) * self.db.get_idf().get_word(word)

    def filter_query_list(self, query):
        logger.info(f"Filtering the query: '{query}'...")
        filtered_list = all_filters(query, self.db)
        logger.info(f"Finished filtering: '{filtered_list}'")
        return filtered_list

    def searching_word(self, word: str):
        for web in self.db.get_scores()[word]:
            if web not in self.scorings:
                self.scorings[web] = self.db.get_scores()[word][web]
            else:
                self.scorings[web] = self.scorings[web] + self.db.get_scores()[word][web]

    def scoring_to_results(self):
        return sorted(self.scorings.items(), key=lambda item: item[1], reverse=True)[:3]

    def searching_query(self, query: str):
        try:
            logger.info(f"Starts searching for '{query}'")
            query_list = self.filter_query_list(query)
            self.scorings: dict[str, float] = {}

            for word in query_list:
                logger.info(f"Searching for word '{word}'")
                self.searching_word(word)

            results = self.scoring_to_results()
            logger.info(f"Found results: {results}")
            return results

        except Exception as error:
            logger.error(error)
            raise Exception(error)


    def print_results(self, results: List[set]):
        try:

            if len(results) > 3: logger.error("The results are mote than 3"); raise Exception("The results are mote than 3")
            for i in range(len(results)):
                print(f"\033[1m{i + 1}s place:\033[0m {results[i][0]}, with accuracy of {results[i][1]}")

        except Exception as error:
            logger.error(error)
            raise Exception(error)
