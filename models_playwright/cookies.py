import json
from pathlib import Path

class Cookies:
    def __init__(self, context): 
        self.context = context 
        
    async def get_async(self):
        cookies = await self.context.cookies()
        Path("cookies.json").write_text(json.dumps(cookies))
    
    async def set_async(self):
        await self.context.add_cookies(json.loads(Path("cookies.json").read_text()))
        
