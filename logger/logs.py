from .settings import Settings

SETTINGS: Settings
   
def set_up_logger(multiple_documents = False):
    global SETTINGS
    SETTINGS = Settings(multiple_documents)
    
def set_logger(function_name):
    return Settings._set_logger(function_name, SETTINGS.file_handler)

    

