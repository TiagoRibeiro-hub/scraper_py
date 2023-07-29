from scrape_ops.utils import Utils
from scrape_ops.agent import Agent
import asyncio

class ScrapeOpsAgent(Agent):
    def __init__(
        self, 
        api_key: str, 
        num_results: str, 
        endpoint: str, 
        enabled: bool,
        repeat_list: bool
        ):
        super().__init__(
            api_key,
            num_results,
            endpoint,
            enabled,
            repeat_list,
            )
    
    async def set_headers_list_async(self):
        if Utils.is_scrapeops_fake_headers_enabled(self.api_key, self.enabled):
                await self._set_headers_list_async()
        else:
          raise Exception('Invalid Scrape Ops values') 
         
    async def _set_headers_list_async(self): 
        if len(self._headers_list) == 0:     
            self._headers_list = await Utils.get_headers_list_async(
                                    self.api_key, 
                                    self.num_results, 
                                    self.endpoint)
               
    def get_unused_list(self):
        return self._headers_list
        
    async def _get_random_header_async(self):
        random_index = Utils.get_random(self._headers_list)
        if self.repeat_list is False:
            result = self._headers_list.pop(random_index)      
            if len(self._headers_list) == 0: 
                await self._set_headers_list_async()
            return result
        else:
            return self._headers_list[random_index]
        
    async def get_async(self):
        pass