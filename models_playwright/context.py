class Context:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url
    
    async def set_async(self):
        # user_agent = self.get_user_agent()
        return await self.browser.new_context(
                base_url= self.base_url,
                # user_agent= user_agent
                # extra_http_headers=
            )
        
    def get_user_agent(self):
        # TODO
        pass