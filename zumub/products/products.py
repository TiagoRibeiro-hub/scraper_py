from playwright.async_api import async_playwright
import asyncio
from pathlib import Path
import json
# * ---
from logger import Log
from models_playwright import Action, Browser
from zumub.products.models.product import Product

class Products:
    async def get_async():
            try:
                async with async_playwright() as p:
                    browser = await Browser.get_async(p, True)
                    total_pages = await Product.get_total_pages(browser)
                    Log.info("Total Pages", f'Nr pages {total_pages}')         
                    
                    tasks = []
                    for i in range(total_pages):
                        tasks.append(Product.get_products_by_page(browser, (i + 1)))
                        
                    products_lists = await asyncio.gather(*tasks)
                    products = []
                    for product in products_lists:
                        products += product     
                    
                    Log.info("Products Tasks Ends", f'Products {len(products)}')
                    if len(products):
                        Path("zumub_data/products.json").write_text(json.dumps(products))  

                    await browser.close()
            except Exception as e:
                Action.cancel_all_tasks(e) 


          
