from playwright.async_api import async_playwright
import asyncio
# * ---
from scrape.models_playwright import Action, Cookies, Browser, Context
from scrape.interceptors import Interceptor
from constants import BASE_URL, ZUMUB_COOKIES_PATH

class Checkout:          
    async def go_async():
        async with async_playwright() as p:
            browser = await Browser.get_async(p, False)
            context = await Context(browser, BASE_URL).set_async()
            await Cookies(context, ZUMUB_COOKIES_PATH).set_async()  
            page = await context.new_page() 
            await page.route('**/*', Interceptor.block)
            # TODO checkout
            await page.goto('')  
            print(await page.title())
            await asyncio.sleep(10)
            await Action.close_async(browser, context) 


                   