import logging as log


def logger(path: str, message: str, intention: str):
    """
    Logs a messages to the specified file with a given intention.

    Args:
        path (str): The file path where logs should be written.
        message (str): The messages to log.
        intention (str): The intention of the log (e.g., 'INFO', 'ERROR').

    Returns:
        None
    """
    # Define the logging configuration
    log.basicConfig(
        filename=path,
        level=log.DEBUG,  # Log all levels from DEBUG and above
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Get a logger instance
    logs = log.getLogger()

    # Log the messages based on the intention
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