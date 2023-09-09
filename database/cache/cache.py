from IndexedRedis import setDefaultRedisConnectionParams
class Cache:
    @staticmethod
    def connect():
        setDefaultRedisConnectionParams({ 'host' : '127.0.0.1', 'port' : 6379, 'db' : 0 })