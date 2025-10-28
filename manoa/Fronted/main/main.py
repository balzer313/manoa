from Fronted.Client.Client import client
from Fronted.logs.Log import logger


if __name__ == "__main__":
    client = client()
    logger.info("Client created")
    client.start()
