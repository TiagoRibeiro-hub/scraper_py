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
                    nr_pages = total_pages['total_pages']
                    total_products_page = int(total_pages['total_products_page'])
                    Log.info("Total Pages", f'Nr pages {nr_pages}')         
                    Log.info("Total Products", f'Nr total products per page {total_products_page}')
                    
                    tasks = []
                    if nr_pages > 1:
                        for i in range(nr_pages):
                            tasks.append(
                                Product.get_products_by_page(
                                    browser, 
                                    product_name, 
                                    (i + 1),
                                    total_products_page)
                                )
                    else:
                        tasks.append(
                            Product.get_products_by_page(
                                browser, 
                                product_name, 
                                None,
                                total_products_page)
                            )
                    
                    products_lists = await asyncio.gather(*tasks)
                    await browser.close()    
                                         
                products = []
                for product in products_lists:
                    products += product     
                
                Log.info("Products Tasks Ends", f'Products {len(products)}')
                products_json = json.dumps(products)
                if len(products):
                    Path(f"{ZUMUB_DATA_PATH}products_{product_name}.json").write_text(products_json)  
                  
                return products_json
            except Exception as e:
                raise Exception(e)


          
