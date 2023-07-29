import asyncio
from contextlib import suppress
from playwright.async_api  import async_playwright
from action import Action   
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from constants import BASE_URL, ZUMBU

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
        await Action.close_async(browser, context) 
        
async def get_zumub_products_async():
    async with async_playwright() as p:
        browser = await Browser.get_async(p, True)
        context = await Context(browser, BASE_URL).set_async()
        page = await context.new_page() 
        await page.route('**/*', Interceptor.block)
        await page.goto(ZUMBU) 
        # TODO products      
        print(await page.title())
        await Action.close_async(browser, context)
       
async def login_get_cookies_async():
    async with async_playwright() as playwright:
        await Action.login_get_cookies_async(playwright)

asyncio.run(main())

if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

        # Cancel all running tasks:
        pending = asyncio.Task.all_tasks()
        for task in pending:
            task.cancel()
            # Now we should await task to execute it's cancellation.
            # Cancelled task raises asyncio.CancelledError that we can suppress:
            with suppress(asyncio.CancelledError):
                loop.run_until_complete(task)
    except:
        pass
                   
