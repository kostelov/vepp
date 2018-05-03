import os
import logging
import logging.handlers

LOG_FOLDERS_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(LOG_FOLDERS_PATH, 'update.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
update_logger = logging.getLogger('update')
update_handler = logging.FileHandler(LOG_FILE_PATH, encoding='utf-8')
update_handler.setLevel(logging.INFO)
update_logger.addHandler(update_handler)
update_handler.setFormatter(formatter)
update_logger.setLevel(logging.INFO)