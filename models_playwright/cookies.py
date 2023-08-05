import json
from pathlib import Path
from logger.logger import Logger

class Cookies:
    def __init__(self, context): 
        self.context = context 
        
    async def get_async(self):
        try:
            cookies = await self.context.cookies()
            Path("cookies.json").write_text(json.dumps(cookies))
            Logger.info('COOKIES', f'Cookies are loaded')  
        except Exception as e:
            Logger.error('COOKIES', f'Something went wrong, {e}')          
            raise Exception(e)
        
    async def set_async(self):
        try:
            cokkies = json.loads(Path("cookies.json").read_text())
        except Exception as e:
            Logger.error('COOKIES', f'Not possible to load cookies, {e}')          
            raise Exception(e)      
        finally:
            await self.context.add_cookies(cokkies)
            Logger.info('COOKIES', f'Cookies are added')  
        
