import os
import json
import shutil
# * ---
from logger import Log

class Files:
    @staticmethod
    def root_dir():
        root_dir = os.path.dirname(os.path.abspath(__file__))
        Log.info('ROOT DIR', f'{root_dir}')
        return root_dir
    
    @staticmethod
    def create_dir(path):
        try:
            file_name_index = path.rfind('/') + 1   
            path = path[0:file_name_index]
            if not os.path.exists(path):
                    os.makedirs(path)
        except OSError as e:
            Log.error('FUNC: CREATE_DIR', 
                      f'Error occurred while create a directory.\n ERROR: {e}'
                      )
                
    @staticmethod          
    def write_json(path, mode, text):  
        try:
            json_payload = json.dumps(text, ensure_ascii=False).encode('ascii', 'ignore').decode('utf-8') 
            with open(file=f'{path}.json', mode=mode, encoding='utf-8') as f:
                f.write(json_payload)
                
            return json_payload
        except OSError as e:
            Log.error('FUNC: WRITE_JSON', 
                      f'Error occurred while write json file.\n ERROR: {e}'
                      )
    
    @staticmethod          
    def read_json(path):  
        try:
            with open(file=f'{path}.json', mode='r', encoding='utf-8') as f:
                return json.load(f)
                
        except OSError as e:
            Log.error('FUNC: READ_JSON', 
                      f'Error occurred while read json file.\n ERROR: {e}'
                      )
            
    @staticmethod  
    def delete(path):
        try:
            os.remove(path)
        except OSError as e:
            Log.error('FUNC: DELETE', 
                      f'Error occurred while deleting file.\n ERROR: {e}'
                      )
                  
    @staticmethod  
    def delete_all_files_in_directory(directory_path):
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    if entry.is_file():
                        os.unlink(entry.path)
        except OSError as e:
            Log.error('FUNC: DELETE_FILES_IN_DIRECTORY', 
                      f'Error occurred while deleting all files.\n ERROR: {e}'
                      )
           
    @staticmethod  
    def delete_all_files_and_sub_directories(directory_path):
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    if entry.is_file():
                        os.unlink(entry.path)
                    else:
                        shutil.rmtree(entry.path)      
        except OSError as e:
            Log.error('FUNC: DELETE_FILES_AND_SUB_DIRECTORIES', 
                      f'Error occurred while deleting files and subdirectories.\n ERROR: {e}'
                      )

        