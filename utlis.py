import logging as log


def logger(path: str, message: str, intention: str):
    logs = log.getLogger(path)

    if not logs.handlers:
        logs.setLevel(log.DEBUG)

        file_handler = log.FileHandler(path)
        file_handler.setLevel(log.DEBUG)

        formatter = log.Formatter('%(asctime)s - %(levelname)s - %(message)s', '%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)

        logs.addHandler(file_handler)

    if intention.upper() == 'DEBUG':
        logs.debug(message)
    elif intention.upper() == 'INFO':
        logs.info(message)
    elif intention.upper() == 'WARNING':
        logs.warning(message)
    elif intention.upper() == 'ERROR':
        logs.error(message)
    elif intention.upper() == 'CRITICAL':
        logs.critical(message)
    else:
        logs.error(f"Invalid intention '{intention}' provided. Message: {message}")
