import logger.logs as logs

class Logger():   
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

    def config_logger(multiple_documents = False):
        logs.config_logger(multiple_documents)