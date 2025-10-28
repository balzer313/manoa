
from Fronted.logs.Log import logger
import yaml


class Config:
    @staticmethod
    def load_config():
        try:
            logger.info("Loading config...")
            config_path = r"C:\Users\Yehonatan\PycharmProjects\manoa\FileInfos\config\config.yml"
            with open(config_path, 'r') as config_file:
                config = yaml.safe_load(config_file)
            logger.info("Finished loading config!")
            return config
        except Exception as error:
            logger.error(error)
            return None