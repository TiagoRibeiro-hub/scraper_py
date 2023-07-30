import logger.logs as logs

class Logger():   
    def info(function_name, message):
        logs.set_logger(function_name).info(message)
    
    def warning(function_name, message):
        logs.set_logger(function_name).warning(message)

    def error(function_name, message):
        logs.set_logger(function_name).error(message)
        
    def critical(function_name, message):
        logs.set_logger(function_name).critical(message)

    def set_up_logger(multiple_documents = False):
        logs.set_up_logger(multiple_documents)