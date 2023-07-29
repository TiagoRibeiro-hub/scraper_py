from scrape_ops_utils import ScrapeOpsUtils, SCRAPEOPS_IO_API_KEY, SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT, SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED, SCRAPEOPS_NUM_RESULTS

class BrowserHeaderAgent:
    async def __init__(self):
        self.scrapeops_api_key = SCRAPEOPS_IO_API_KEY
        self.scrapeops_endpoint = SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT
        self.scrapeops_fake_browser_headers_active = SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED
        self.scrapeops_num_results = SCRAPEOPS_NUM_RESULTS
        self.headers_list = []
        if ScrapeOpsUtils.is_scrapeops_fake_headers_enabled(self.scrapeops_api_key, self.scrapeops_fake_browser_headers_active):
            await self._get_headers_list()
        else:
            raise Exception('Invalid Scrape Ops values')

    def _get_headers_list(self):      
        self.headers_list = ScrapeOpsUtils.get_headers_list(self.scrapeops_api_key, self.scrapeops_num_results, self.scrapeops_endpoint)
         
    def _get_random_browser_header(self):
        return ScrapeOpsUtils.get_random(self.headers_list)
    
    def get_browser_headers(self):        
        random_browser_header = self._get_random_browser_header()
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
         

        
