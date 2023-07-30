from pathlib import Path
import datetime as dt
import os
import yaml
import logging

ROOT_DIR = Path.cwd()

class Settings:
    def __init__(self, multiple_documents = False):
        self.multiple_documents = multiple_documents
        self.console_level = logging.DEBUG
        self.log_file_level = logging.WARNING
        self.file_input_format = '%(asctime)s: %(levelname)s - %(message)s'
        self.path = self._set_configuration()
        
    def _set_configuration(self) -> str:
        with open(f'{ROOT_DIR}/config.yaml', 'r') as f:
            try:
                config = None
                if self.multiple_documents is True:
                    configs = yaml.safe_load_all(f)
                    config = configs['logger']
                else:
                    config = yaml.safe_load(f)
                
                if config is None:
                    raise Exception("yaml config failed") 
                
                path = self._set_props(config['logger'])
                return self._set_path(path)
            
            except Exception as e:
                print("yaml failed. ", e)

    def _set_path(self, path):
        if path is None:
            path = f'{ROOT_DIR}/logs'
        if not os.path.exists(path):
            os.makedirs(path)
            print("The logs directory is created!")
        elif path.endswith('/'):
            path[:-1]
                
        today = dt.datetime.today()
        file_name = f'{today.month:02d}-{today.day:02d}-{today.year}.log'             
        return f'{path}/{file_name}'
                
    def _set_props(self, config) -> str:   
        self.file_input_format = config['file_input_format']
        self._set_console_level(config['console_level'])
        self._set_log_file_level(config['log_file_level'])
        return config['path']

    def _set_console_level(self, level):
        if isinstance(level, int):
            result = self._set_level(level)
            if result is not None:
                self.console_level = result
                
    def _set_log_file_level(self, level):
        if isinstance(level, int):
            result = self._set_level(level)
            if result is not None:
                self.log_file_level = result
                 
    def _set_level(self, level: int):
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