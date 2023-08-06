import json
import math
from pathlib import Path
from playwright.async_api import async_playwright
import asyncio
import action  
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from constants import BASE_URL, ZUMBU, PAGE_EQUALS
from logger.logger import Logger
from models_zumbu.product import Product

async def main():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=True)
        # page = await browser.new_page()
        # await page.goto(f'{BASE_URL}{ZUMBU}')
        # total_page = await action.total_pages(page)
        # await page.close()    
        try:
            Logger.set_configuration_logger()
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
        await page.goto(f'{ZUMBU}')
        total_pages = await action.total_pages(page)
        await context.close()
        Logger.info("Total Pages", f'Nr pages {total_pages}')
             
        tasks = []
        for i in range(total_pages):
            tasks.append(action.get_products_by_page(browser, (i + 1)))
            
        products_lists = await asyncio.gather(*tasks)
        products = []
        for product in products_lists:
            products += product     
        
        Logger.info("Products Tasks Ends", f'Products {len(products)}')
        if len(products):
            Path("json_files/products.json").write_text(json.dumps(products))  

        await browser.close()

   
async def login_get_cookies_async():
    async with async_playwright() as playwright:
        await action.login_get_cookies_async(playwright)

asyncio.run(main())

                   