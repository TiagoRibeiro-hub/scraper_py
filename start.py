import asyncio
from playwright.async_api  import async_playwright
import action  
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from constants import BASE_URL, ZUMBU
from logger.logs import set_up_logger
async def main():
    try:
        set_up_logger()
        tasks = [
            get_zumub_products_async(), 
            login_get_cookies_async()
            ]
        await asyncio.gather(*tasks)
        await checkout_async() 
    except Exception as e:
        action.cancel_all_tasks(e)
            
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
        await action.close_async(browser, context) 
        
async def get_zumub_products_async():
    async with async_playwright() as p:
        browser = await Browser.get_async(p, True)
        context = await Context(browser, BASE_URL).set_async()
        page = await context.new_page() 
        await page.route('**/*', Interceptor.block)
        await page.goto(ZUMBU) 
        # TODO products      
        print(await page.title())
        await action.close_async(browser, context)
       
async def login_get_cookies_async():
    async with async_playwright() as playwright:
        await action.login_get_cookies_async(playwright)

asyncio.run(main())

                   