import logger.logs as logs

def debug(logger_name, message):
    logs.set_logger(logger_name).debug(message)


def info(logger_name, message):
    logs.set_logger(logger_name).info(message)


def warning(logger_name, message):
    logs.set_logger(logger_name).warning(message)


def error(logger_name, message):
    logs.set_logger(logger_name).error(message)


def critical(logger_name, message):
    logs.set_logger(logger_name).critical(message)


def set_configuration(multiple_documents = False):
    logs.set_settings(multiple_documents)