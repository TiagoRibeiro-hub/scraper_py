from global_imports import Path, json

class Cookies:
    def __init__(self, context): 
        self.context = context 
        
    async def get(self):
        cookies = await self.context.cookies()
        Path("cookies.json").write_text(json.dumps(cookies))
    
    async def set(self):
        await self.context.add_cookies(json.loads(Path("cookies.json").read_text()))
        