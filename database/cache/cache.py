from datetime import datetime, time
import redis
# * ---
from IndexedRedis import setDefaultRedisConnectionParams
class Cache:
    @staticmethod
    def connectIndexedRedis():
        setDefaultRedisConnectionParams({ 'host' : '127.0.0.1', 'port' : 6379, 'db' : 0 })
        
    @staticmethod
    def connect():
        return redis.Redis(
            host='127.0.0.1',  
            port=6379, 
            db=0, 
            decode_responses=True)
    
    @staticmethod
    def get_expire_date():
        return int(datetime.combine(datetime.now(), time.max).strftime('%Y%m%d%H%M%S'))