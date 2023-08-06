from playwright.async_api import async_playwright
import asyncio
import models_playwright.action as action  
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from zumub.constants import BASE_URL
from logger import *

async def main():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=True)
        # page = await browser.new_page()
        # await page.goto(f'{BASE_URL}{ZUMBU}')
        # total_page = await action.total_pages(page)
        # await page.close()    
        try:
            logger.set_configuration()
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

asyncio.run(main())

                   