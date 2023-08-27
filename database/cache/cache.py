import redis
import json
# * ---
from enviroment import REDIS_ENV
REDIS = None
class Cache:
    @staticmethod
    def connect():
        global REDIS
        REDIS = redis.Redis(
            host=REDIS_ENV['HOST_REDIS'], 
            password=REDIS_ENV['REDIS_PASS'], 
            port=REDIS_ENV['PORT_REDIS'], 
            db=0, 
            decode_responses=True)
        
    @staticmethod
    def set(category: str, page_nr: str, value: str):
        REDIS.set(f'{category}_{page_nr}', json.dumps(value, ensure_ascii=False).encode('ascii', 'ignore').decode('utf-8'))
    
    @staticmethod
    def get(category: str, page_nr: str):
        return REDIS.get(f'{category}_{page_nr}')