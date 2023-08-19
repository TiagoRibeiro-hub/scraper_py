from scrape.interceptors import Interceptor
from constants import PAGE_EQUALS, SORT_BY_NAME, ZUMUB_DATA_PATH
from logger import Log
from utils import Files
from scrape.zumub.utils.js_evaluate import JS_Evaluate

class Product:  
    @staticmethod
    async def get_async(page, category = ''):
        try:
            await Product.__page_route(page, f'{category}?{SORT_BY_NAME}', 'div.inner-product-box')
            products = await page.evaluate(JS_Evaluate.get_products()) 
            return products        
        except Exception as e:
            Log.error('FUNC: GET_PRODUCTS_ASYNC', f'Somenthing went wrong, {e}')          
            raise Exception(e) 
        
    @staticmethod
    async def get_by_page_async(page, category, page_nr):
        try:
            await Product.__page_route(page, f'{category}?{SORT_BY_NAME}&{PAGE_EQUALS}{page_nr}', 'div.inner-product-box')
            products = await page.evaluate(JS_Evaluate.get_products()) 
            return products
        except Exception as e:
            Log.error('FUNC: GET_PRODUCTS_BY_PAGE_ASYNC', f'Somenthing went wrong, {e}')          
            raise Exception(e) 
        
    @staticmethod
    async def get_total_pages_async(page, category) -> int:
        try:
            await Product.__page_route(page, f'{category}', 'div.pagination')
            pagination = await page.query_selector('div.pagination p')
            return await pagination.evaluate(JS_Evaluate.get_total_page())
        except Exception as e:
            Log.error('FUNC: GET_TOTAL_PAGES_ASYNC', f'Somenthing went wrong, {e}')          
            raise Exception(e) 
      
    @staticmethod
    async def __page_route(page, goto: str, is_visible: str):
        await page.route('**/*', Interceptor.block) 
        await page.goto(goto)
        await page.is_visible(is_visible)
        
    @staticmethod
    def save_json(category, products_lists):
        products_client = []
        products_links = []
        for product in products_lists:
            products_client.append(product['data_client'])
            products_links.append(product['data_links'])
            
        products_client_json = None
        if len(products_client):
            products_client_json = Files.write_json(f"{ZUMUB_DATA_PATH}products_{category}", 'w', products_client)
        if len(products_links):
            Files.write_json(f"{ZUMUB_DATA_PATH}products_links_{category}", 'w', products_links)
        return products_client_json
