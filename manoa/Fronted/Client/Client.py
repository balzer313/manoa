from Backened.Engine.Engine import Engine
from Fronted.logs.Log import logger


class client():
    def __init__(self):
        logger.info("system started")
        self.engine = Engine()


    def start(self):
        print("==================\nWelcome to G877LE!\n==================\n")
        while True:
            try:
                search_input = str(input("=-=-=-=-=-=-=-=-=-=-=-=\nenter your search: "))
                logger.info(f"user search is {search_input}")
                self.engine.print_results(self.engine.searching(search_input))
                print("=-=-=-=-=-=-=-=-=-=-=-=\n")
            except Exception as error:
                logger.error(error)
                return


if __name__ == "__main__":
    client = client()
    client.start()
