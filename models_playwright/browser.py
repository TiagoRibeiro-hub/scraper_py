class Browser:   
    async def get_async(p, headless):
        return await p.chromium.launch(
                            headless=headless, 
                            slow_mo=50,
                            # devtools=True,
                            )