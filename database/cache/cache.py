import redis
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
    def set_per_category(category: str, page_nr: str, value: str):
        REDIS.json().set(
            f'{category}:{page_nr}', 
            '$', 
            value
            )
    
    @staticmethod
    def set(key: str, value: str):
        REDIS.set(
            key, 
            value
            )
  
    @staticmethod
    def get_per_category(category: str, page_nr: int):
        return REDIS.json().get(f'{category}:{page_nr}')
    
    @staticmethod
    def get(key: str):
        return REDIS.get(key)
    