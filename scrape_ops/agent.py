from abc import abstractmethod

class Agent:
    def __init__(
        self, 
        api_key: str, 
        num_results: str, 
        endpoint: str, 
        enabled: bool,
        repeat_list: bool
        ):
        self.api_key = api_key
        self.num_results = num_results
        self.endpoint = endpoint
        self.enabled = enabled
        self.repeat_list = repeat_list
        self._headers_list = []
    
    @abstractmethod
    async def set_headers_list_async(self):
        pass
    
    @abstractmethod
    async def _set_headers_list_async(self): 
        pass
    
    @abstractmethod
    def get_unused_list(self):
        pass
    
    @abstractmethod
    async def _get_random_header_async(self):
        pass
    
    @abstractmethod
    async def get_async(self):
        pass