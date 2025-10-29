from source.Client.Client import client
from config.Log import logger


if __name__ == "__main__":
    client = client()
    logger.info("Client created")
    client.start()
