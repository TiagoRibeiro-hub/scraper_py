from playwright.async_api import async_playwright
import asyncio
from logger.logger import Logger
from models_playwright.browser import Browser
import models_playwright.action as action
import json
from pathlib import Path
from zumub.products.models.product import Product

async def main():
    async with async_playwright() as p:
        try:
            Logger.set_configuration_logger()
            await get_zumub_products_async()
        except Exception as e:
            action.cancel_all_tasks(e) 

async def get_zumub_products_async():
    async with async_playwright() as p:
        browser = await Browser.get_async(p, True)
        total_pages = await Product.get_total_pages(browser)
        Logger.info("Total Pages", f'Nr pages {total_pages}')         
        
        tasks = []
        for i in range(total_pages):
            tasks.append(Product.get_products_by_page(browser, (i + 1)))
            
        products_lists = await asyncio.gather(*tasks)
        products = []
        for product in products_lists:
            products += product     
        
        Logger.info("Products Tasks Ends", f'Products {len(products)}')
        if len(products):
            Path("json_files/products.json").write_text(json.dumps(products))  

        await browser.close()
          
asyncio.run(main())