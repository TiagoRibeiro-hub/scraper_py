from .settings import logging, Settings

FILE_HANDLER: logging.FileHandler

class Logger():     
    def info(logger_name, message):
        _set_logger(logger_name).log(logging.INFO, message)
    
    def warning(logger_name, message):
        _set_logger(logger_name).logging.log(logging.WARNING, message)

    def error(logger_name, message):
        _set_logger(logger_name).logging.log(logging.ERROR, message)
        
    def critical(logger_name, message):
        _set_logger(logger_name).logging.log(logging.CRITICAL, message)


def _set_logger(logger_name) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.addHandler(FILE_HANDLER)
    return logger

def set_up_logger(multiple_documents = False):
    settings = Settings(multiple_documents)
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    
    logging.basicConfig(level=settings.console_level)

    FILE_HANDLER = logging.FileHandler(settings.path)
    FILE_HANDLER.setLevel(settings.log_file_level)
    FILE_HANDLER.setFormatter(logging.Formatter(settings.file_input_format))

