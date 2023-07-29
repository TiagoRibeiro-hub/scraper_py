import httpx
from urllib.parse import urlencode
from random import randint

# ! SCRAPEOPS_API
# * USER_AGENT
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True
# * BROWSER_HEADER
SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True

# ! Methods
class Utils:  
    async def get_headers_list_async(scrapeops_api_key, scrapeops_num_results, scrapeops_endpoint):
        payload = {
            'api_key': scrapeops_api_key,
            'num_headers': scrapeops_num_results
            }   
        async with httpx.AsyncClient() as client: 
            response = await client.get(scrapeops_endpoint, params=urlencode(payload))
            return response.json().get('result', [])

    def is_scrapeops_fake_headers_enabled(scrapeops_api_key, scrapeops_fake_header_active):
        if scrapeops_api_key is None or scrapeops_api_key == '' or scrapeops_fake_header_active == False:
            return False
        else:
            return True

    def get_random(list) -> int: 
        return randint(0, len(list) - 1)