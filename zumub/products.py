from playwright.async_api import async_playwright
import asyncio
from constants import ZUMUB_DATA_PATH
# * ---
from logger import Log
from models_playwright import Browser
from zumub.models.product import Product
from utils_files import Files

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
                                              
                products_client = []
                products_links = []
                for products in products_lists:
                    for product in products:
                        products_client.append(product['data_client'])
                        products_links.append(product['data_links'])
                
                Log.info("Products Tasks Ends", f'Products {len(products_client)}')
                products_client_json = None
                if len(products_client):
                    products_client_json = Files.write_json(f"{ZUMUB_DATA_PATH}products_{product_name}", 'w', products_client)
                if len(products_links):
                    Files.write_json(f"{ZUMUB_DATA_PATH}products_links_{product_name}", 'a', products_links)
                     
                return products_client_json
            except Exception as e:
                raise Exception(e)


          
