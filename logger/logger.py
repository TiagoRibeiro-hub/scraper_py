import logger.logs as logs

class Logger(): 
    @staticmethod  
    def debug(logger_name, message):
        logs.set_logger(logger_name).debug(message)
    
    @staticmethod  
    def info(logger_name, message):
        logs.set_logger(logger_name).info(message)
    
    @staticmethod
    def warning(logger_name, message):
        logs.set_logger(logger_name).warning(message)

    @staticmethod
    def error(logger_name, message):
        logs.set_logger(logger_name).error(message)
    
    @staticmethod  
    def critical(logger_name, message):
        logs.set_logger(logger_name).critical(message)

    @staticmethod
    def set_configuration_logger(multiple_documents = False):
        logs.set_settings(multiple_documents)