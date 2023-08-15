from playwright.async_api import async_playwright
# * ---
from models_playwright import Browser, Context, Action
from zumub.utils.product import Product
from constants import BASE_URL

class Products:
    @staticmethod
    async def get_async(link):
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)  
                context = await Context(browser, link).set_async()
                page = await context.new_page()              
                products_lists = await Product.get_async(page)               
                await Action.close_async(browser, context)
     
            category = link[(link.rfind('/') + 1):]
            return Product.save_json(category, products_lists)

        except Exception as e:
            raise Exception(e)
    
    @staticmethod
    async def get_by_category_async(category):
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)  
                context = await Context(browser, BASE_URL).set_async()
                page = await context.new_page()              
                products_lists = await Product.get_async(page, category)               
                await Action.close_async(browser, context)
     
            return Product.save_json(category, products_lists)

        except Exception as e:
            raise Exception(e)   
        
    @staticmethod
    async def get_by_page_async(category, page_nr):
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)  
                context = await Context(browser, BASE_URL).set_async()
                page = await context.new_page()                      
                products_lists = await Product.get_by_page_async(
                                page, 
                                category, 
                                page_nr)              
                await Action.close_async(browser, context)                
            return Product.save_json(category, products_lists)
        except Exception as e:
            raise Exception(e)
        
    @staticmethod
    async def get_total_pages_async(category):
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)  
                context = await Context(browser, BASE_URL).set_async()
                page = await context.new_page()                           
                return await Product.get_total_pages_async(page, category)
        except Exception as e:
            raise Exception(e)
          
