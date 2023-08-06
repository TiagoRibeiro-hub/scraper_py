from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from zumub.constants import BASE_URL, PAGE_EQUALS, ZUMBU
from logger.logger import Logger
import js.js as JS

class Product:   
    
    @staticmethod
    async def get_products_by_page(browser, nr):
        context = await Context(browser, BASE_URL).set_async()
        page = await context.new_page()
        await page.route('**/*', Interceptor.block)
        await page.goto(f'{ZUMBU}{PAGE_EQUALS}{nr}')  
        await page.is_visible('div.inner-product-box')  
        products_boxes = await page.query_selector_all('div.inner-product-box')
        products = []
        count_sold_off = 0
        for product_box in products_boxes:
            product = await product_box.evaluate(JS.get_product()) 
            if product is None:
                count_sold_off += 1 
            else:   
                products.append(product)
            if count_sold_off > 3:
                break
        await context.close()
        return products
    
    @staticmethod
    async def get_total_pages(browser) -> int:
        try:
            context = await Context(browser, BASE_URL).set_async()
            page = await context.new_page() 
            await page.route('**/*', Interceptor.block)
            await page.goto(f'{ZUMBU}')
            await page.is_visible('div.pagination')   
            pagination = await page.query_selector('div.pagination p')
            total_pages = await pagination.evaluate(JS.get_total_page)
            await context.close()
            return total_pages
        
        except Exception as e:
            Logger.error('FUNC: TOTAL_PAGES', f'Somenthing went wrong, {e}')          
            raise Exception(e)    
    