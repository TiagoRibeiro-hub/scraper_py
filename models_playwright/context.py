from scrape_ops.browser_agent import BrowserHeaderAgent
import asyncio
from constants import SCRAPEOPS_NUM_RESULTS, SCRAPEOPS_IO_API_KEY

class Context:
    def __init__(self, browser, base_url):
        self.browser_header_agent_task = BrowserHeaderAgent(
            SCRAPEOPS_IO_API_KEY, 
            SCRAPEOPS_NUM_RESULTS, 
            False
            ).set_headers_list_async()
        self.browser = browser
        self.base_url = base_url
    
    async def set_async(self):
        headers = await self._get_browser_header_async()
        if headers is None:
            raise Exception('BrowserHeaderAgent response is none')
        return await self.browser.new_context(
                base_url= self.base_url,
                extra_http_headers= headers
            )
        
    async def _get_browser_header_async(self):
        print("self.browser_header_agent_task: ", self.browser_header_agent_task)
        browser_header_agent = await asyncio.gather(self.browser_header_agent_task)
        print("browser_header_agent: ", browser_header_agent)
        if browser_header_agent:
            return await browser_header_agent.get_async()
        else:
            raise Exception('BrowserHeaderAgent init task failed')