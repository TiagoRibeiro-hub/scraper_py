from playwright.async_api  import async_playwright
from global_imports import asyncio, BASE_URL, ZUMBU, Login, EMAIL, PASSWORD, Browser, Context, Cookies, Interceptor
    
async def main():
    tasks = [
        get_zumub_products_async(), 
        login_get_cookies_async()
        ]
    await asyncio.gather(*tasks)
    await checkout_async() 

async def checkout_async():
    async with async_playwright() as p:
        browser = await Browser.get_async(p, False)
        context = await Context(browser, BASE_URL).set_async()
        await Cookies(context).set_async()  
        page = await context.new_page() 
        await page.route('**/*', Interceptor.block)
        # TODO checkout
        await page.goto('')  
        print(await page.title())
        await asyncio.sleep(10)
        await close_async(browser, context) 
        
async def get_zumub_products_async():
    async with async_playwright() as p:
        browser = await Browser.get_async(p, True)
        context = await Context(browser, BASE_URL).set_async()
        page = await context.new_page() 
        await page.route('**/*', Interceptor.block)
        await page.goto(ZUMBU) 
        # TODO products      
        print(await page.title())
        await close_async(browser, context)
        
async def login_get_cookies_async():
    async with async_playwright() as p:
        browser = await Browser.get_async(p, False)
        # * set context for login, get page, submit add get cookies
        context = await Context(browser, BASE_URL).set_async()    
        cookies = Cookies(context)            
        page = await context.new_page() 
        await page.route('**/*', Interceptor.block)
        await page.on("request", Interceptor.request)
        await page.on("response", Interceptor.response)
        await page.goto('')   
        await Login().submit_async(page, EMAIL, PASSWORD)
        await cookies.get_async()     
        await close_async(browser, context)

async def close_async(browser, context):
    await context.close()
    await browser.close()
          
asyncio.run(main())