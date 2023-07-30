from pathlib import Path
import datetime as dt
import os
import yaml
import logging

ROOT_DIR = Path.cwd()
class Singleton(type):
    _instance = {}   
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]   
    
class Settings(metaclass=Singleton):
     
    def __init__(self, multiple_documents = False):  
        self.multiple_documents = multiple_documents
        self.console_level = logging.DEBUG
        self.log_file_level = logging.WARNING
        self.file_input_format = '%(asctime)s: %(levelname)s - %(message)s'
        self.path = ''
        self.file_handler = None
        self.__set_configuration()
        print_message('LOGGER INFO', 'Logger configuration completed successfully.')
        
    def set_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        logger.addHandler(self.file_handler)
        return logger
    
    def __set_configuration(self) -> str:           
        try:       
            with open(f'{ROOT_DIR}/config.yaml', 'r') as f:
                try:
                    config = None
                    if self.multiple_documents is True:
                        docs = yaml.safe_load_all(f)
                        for doc in docs:
                            for k, v in doc.items():
                                if k == 'logger':
                                    config = v
                    else:
                        doc = yaml.safe_load(f)
                        config = doc['logger']
                    
                    if config is None:
                        self.__set_path(None)
                    else:
                        self.__set_props(config)
                        
                    self.__set_up_handler()          
                except Exception as e:
                    print('LOGGER ERROR => yaml failed: ' + e.args)
                finally:
                    self.__default_settings()  
        except:
            self.__default_settings()  

    def __default_settings(self):
        print_message('LOGGER INFO', 'Default settings used')
        self.__set_path(None)
        self.__set_up_handler() 
            
    def __set_up_handler(self):
        for handler in logging.root.handlers:
            logging.root.removeHandler(handler)
        
        logging.basicConfig(level=self.console_level)

        self.file_handler = logging.FileHandler(self.path)
        self.file_handler.setLevel(self.log_file_level)
        self.file_handler.setFormatter(logging.Formatter(self.file_input_format))    
                   
    def __set_props(self, config) -> str:   
        self.__set_file_input_format(config['file_input_format'])         
        self.__set_console_level(config['console_level'])
        self.__set_log_file_level(config['log_file_level'])
        self.__set_path(config['path']) 

    def __set_path(self, path):
        if path is None:
            path = f'{ROOT_DIR}/logs'
        if not os.path.exists(path):
            os.makedirs(path)
            print_message('LOGGER INFO', 'The logs directory is created!')
        elif path.endswith('/'):
            path[:-1]
                
        today = dt.datetime.today()
        file_name = f'{today.month:02d}-{today.day:02d}-{today.year}.log'             
        self.path = f'{path}/{file_name}'
    
    def __set_file_input_format(self, file_input_format):
        if file_input_format is not None:
            self.file_input_format = file_input_format
            
    def __set_console_level(self, level):
        if isinstance(level, int):
            result = self.__set_level(level)
            if result is not None:
                self.console_level = result
                
    def __set_log_file_level(self, level):
        if isinstance(level, int):
            result = self.__set_level(level)
            if result is not None:
                self.log_file_level = result
                 
    def __set_level(self, level: int):
        if level == 1:
            return logging.DEBUG
        elif level == 2:
            return logging.INFO
        elif level == 3:
            return logging.WARNING
        elif level == 4:
            return logging.ERROR
        elif level == 5:
            return logging.CRITICAL
        else:
            return None
        

def print_message(title: str, message: str):   
    def get_lenght(lenght: int):
        lenght = lenght + lenght
        if lenght % 2 != 0:
            lenght = lenght + 1
        return lenght
    
    lenght_title = len(title)
    lenght_message = len(message)
    
    lenght_final: int
    if lenght_title > lenght_message:
        lenght_final = get_lenght(lenght_title)
    else:
        lenght_final = get_lenght(lenght_message)
        
    result = f' {title.strip()} '.center(lenght_final, '*')   
    result += '\n*' + message.center(lenght_final)[1:-1] + '*\n'    
    for i in range(lenght_final):
        result += '*'
    
    print(result + '\n')
