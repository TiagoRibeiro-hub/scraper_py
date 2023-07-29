from scrape_ops.browser_agent import BrowserHeaderAgent
import asyncio

class Context:
    def __init__(self, browser, base_url):
        self.browser_header_agent_task = BrowserHeaderAgent()
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
        browser_header_agent = await asyncio.gather(*[self.browser_header_agent_task])
        if browser_header_agent:
            return browser_header_agent.get_browser_headers()
        else:
            raise Exception('BrowserHeaderAgent init task failed')