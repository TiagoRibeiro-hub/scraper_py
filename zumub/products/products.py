from playwright.async_api import async_playwright
import asyncio
from pathlib import Path
import json
from constants import ZUMUB_DATA_PATH
# * ---
from logger import Log
from models_playwright import Action, Browser
from zumub.products.models.product import Product

class Products:
    @staticmethod
    async def get_async(product_name):
            try:
                async with async_playwright() as p:
                    browser = await Browser.get_async(p, True)
                    total_pages = await Product.get_total_pages(browser, product_name)
                    Log.info("Total Pages", f'Nr pages {total_pages}')         
                    
                    tasks = []
                    for i in range(total_pages):
                        tasks.append(Product.get_products_by_page(browser, product_name, (i + 1)))
                        
                    products_lists = await asyncio.gather(*tasks)
                    products = []
                    for product in products_lists:
                        products += product     
                    
                    Log.info("Products Tasks Ends", f'Products {len(products)}')
                    products_json = json.dumps(products)
                    if len(products):
                        Path(f"{ZUMUB_DATA_PATH}products_{product_name}.json").write_text(products_json)  

                    await browser.close()
                    return products_json
            except Exception as e:
                Action.cancel_all_tasks(e) 


          
