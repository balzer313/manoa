from source.Engine.Engine import Engine
from config.Log import logger


class client():
    def __init__(self):
        logger.info("system started")
        self.engine = Engine()


    def start(self):
        print("\033[1m===================\nWELC🌐ME to \033[94mG\033[91m8\033[93m7\033[94m7\033[92mL\033[91mE\033[0m!\n\033[1m===================\n\033[0m")
        while True:
            try:
                search_input = str(input("=-=-=-=-=-=-=-=-=-=-=-=\n🔎ENTER YOUR SEARCH: "))
                logger.info(f"user search is {search_input}")
                self.engine.print_results(self.engine.searching_query(search_input))
                print("=-=-=-=-=-=-=-=-=-=-=-=\n")
            except Exception as error:
                logger.error(error)
                return


if __name__ == "__main__":
    client = client()
    client.start()
