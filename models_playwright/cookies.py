import json
# * ---
from logger import Log
from utils_files import Files

class Cookies:
    def __init__(self, context, path): 
        self.context = context 
        self.path = path
        
    async def get_async(self):
        try:
            cookies = await self.context.cookies()
            Files.write_json(self.path, 'w', cookies)
            Log.info('COOKIES', f'Cookies are loaded')  
        except Exception as e:
            Log.error('COOKIES', f'Something went wrong, {e}')          
            raise Exception(e)
        
    async def set_async(self):
        try:
            cokkies = Files.read_json(self.path)
        except Exception as e:
            Log.error('COOKIES', f'Not possible to load cookies, {e}')          
            raise Exception(e)      
        finally:
            await self.context.add_cookies(cokkies)
            Log.info('COOKIES', f'Cookies are added')  
        
