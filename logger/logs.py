from .settings import Settings

SETTINGS: Settings
   
def config_logger(multiple_documents = False):
    global SETTINGS
    SETTINGS = Settings(multiple_documents)
    
def set_logger(logger_name):
    return SETTINGS.set_logger(logger_name)

    

