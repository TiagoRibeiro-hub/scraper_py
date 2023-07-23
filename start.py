from playwright.async_api  import async_playwright
from global_imports import asyncio, Login, EMAIL, PASSWORD, Cookies
    
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
                        headless=False, 
                        slow_mo=50
                        )
        # * set context and get page
        context = await browser.new_context(
            base_url='https://www.zumub.com/EN/'
        )    
        cookies = Cookies(context)  
              
        page = await context.new_page() 
        await page.goto('')
        
        # * login submit add get cookies
        await Login().submit_async(page, EMAIL, PASSWORD)
        await cookies.get()
               
        await browser.close()

 
asyncio.run(main())