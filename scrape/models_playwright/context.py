import asyncio
# * ---
from scrape_ops import BrowserHeaderAgent
from constants import SCRAPEOPS_NUM_RESULTS, SCRAPEOPS_IO_API_KEY
from logger import Log

class Context:
    def __init__(self, browser, base_url):
        self.browser_header_agent = BrowserHeaderAgent(
            SCRAPEOPS_IO_API_KEY, 
            SCRAPEOPS_NUM_RESULTS, 
            False
            )
        asyncio.ensure_future(self.browser_header_agent.set_headers_list_async())
        self.browser = browser
        self.base_url = base_url
        self._headers = None
    
    async def set_async(self):
        await self.__get_browser_header_async()
        return await self.browser.new_context(
                base_url= self.base_url,
                extra_http_headers= self._headers
            )
        
    async def __get_browser_header_async(self):
        self._headers = await self.browser_header_agent.get_async()
        if self._headers is None:
            Log.warning('CONTEXT', f'BrowserHeaderAgent response is none')  
            raise Exception('Browser Header Agent response is none')