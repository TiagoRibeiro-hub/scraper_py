from scrape_ops.utils import SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT, SCRAPEOPS_FAKE_USER_AGENT_ENABLED
from scrape_ops.scrape_ops_agent import ScrapeOpsAgent, asyncio

class UserAgent(ScrapeOpsAgent):
    def __init__(
        self, 
        scrapeops_api_key: str, 
        scrapeops_num_results: str, 
        repeat_list: bool
        ):
        super().__init__(
            scrapeops_api_key, 
            scrapeops_num_results, 
            SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT,
            SCRAPEOPS_FAKE_USER_AGENT_ENABLED,
            repeat_list)
    
    async def get_async(self):   
        while len(self._headers_list) == 0:
            await asyncio.sleep(5)  
            
        user_agent = await self._get_random_header_async()   
        return { 'user-agent': user_agent }