from scrape_ops.utils import SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT, SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED
from scrape_ops.scrape_ops_agent import ScrapeOpsAgent

class BrowserHeaderAgent(ScrapeOpsAgent):
    def __init__(
        self, 
        scrapeops_api_key: str, 
        scrapeops_num_results: str, 
        repeat_list: bool
        ):
        super().__init__(
            scrapeops_api_key, 
            scrapeops_num_results, 
            SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT,
            SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED,
            repeat_list)
    
    async def get_async(self):        
        random_browser_header = await self._get_random_header_async()
        return {
            'upgrade-insecure-requests': random_browser_header['upgrade-insecure-requests'],
            'sec-ch-ua': random_browser_header['sec-ch-ua'],
            'sec-ch-ua-mobile': random_browser_header['sec-ch-ua-mobile'],
            'sec-ch-ua-platform': random_browser_header['sec-ch-ua-platform'],
            'sec-fetch-site': random_browser_header['sec-fetch-site'],
            'sec-fetch-mod': random_browser_header['sec-fetch-mod'],
            'sec-fetch-user': random_browser_header['sec-fetch-user'],
            'user-agent': random_browser_header['user-agent'],
            'accept': random_browser_header['accept'],
            'accept-encoding': random_browser_header['accept-encoding'],
            'accept-language': random_browser_header['accept-language']  ,   
        }

