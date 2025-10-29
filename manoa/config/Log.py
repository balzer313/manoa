import logging

logger = logging.getLogger("manoa_log")

from config.configs import *

config = load_config()

try:
    logging.basicConfig(filename=f'{config["paths"]["logs_path"]}/logs.log', level=logging.INFO)

except Exception as e:
    print(e)

