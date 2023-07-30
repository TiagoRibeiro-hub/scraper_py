from .settings import logging, Settings

file_handler = None

def _set_logger(logger_name) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.addHandler(file_handler)
    return logger

def set_up_logger(multiple_documents = False):
    settings = Settings(multiple_documents)
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    
    logging.basicConfig(level=settings.console_level)
 
    file_handler = logging.FileHandler(settings.path)
    file_handler.setLevel(settings.log_file_level)
    file_handler.setFormatter(logging.Formatter(settings.file_input_format))

    
def info(logger_name, message):
    _set_logger(logger_name).log(logging.INFO, message)
  
def warning(logger_name, message):
    _set_logger(logger_name).logging.log(logging.WARNING, message)

def error(logger_name, message):
    _set_logger(logger_name).logging.log(logging.ERROR, message)
    
def critical(logger_name, message):
    _set_logger(logger_name).logging.log(logging.CRITICAL, message)


