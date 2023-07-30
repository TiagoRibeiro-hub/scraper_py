import logging
import datetime as dt
from pathlib import Path

file_handler = None

def _set_logger(logger_name) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.addHandler(file_handler)
    return logger

def set_up_logger(
    path: str = None, 
    level = logging.WARNING, 
    format: str = '%(asctime)s: %(levelname)s - %(message)s'
    ):
    for handler in logging.root.handlers:
        logging.root.removeHandler(handler)
    
    logging.basicConfig(level=logging.DEBUG)

    today = dt.datetime.today()
    file_name = f'{today.month:02d}-{today.day:02d}-{today.year}.log'

    if path is None:
        path = Path.cwd()
    elif path.endswith('/'):
        path[:-1]
    

    file_handler = logging.FileHandler(f'{path}/{file_name}')
    file_handler.setLevel(level)
    file_handler.setFormatter(logging.Formatter(format))

def info(logger_name, message):
    _set_logger(logger_name).log(logging.INFO, message)
  
def warning(logger_name, message):
    _set_logger(logger_name).logging.log(logging.WARNING, message)

def error(logger_name, message):
    _set_logger(logger_name).logging.log(logging.ERROR, message)
    
def critical(logger_name, message):
    _set_logger(logger_name).logging.log(logging.CRITICAL, message)


