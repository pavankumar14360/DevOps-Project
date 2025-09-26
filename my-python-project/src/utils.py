def load_config(file_path):
    import json
    with open(file_path, 'r') as file:
        return json.load(file)

def log_message(message, level='INFO'):
    import logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    if level == 'INFO':
        logger.info(message)
    elif level == 'WARNING':
        logger.warning(message)
    elif level == 'ERROR':
        logger.error(message)
    else:
        logger.debug(message)