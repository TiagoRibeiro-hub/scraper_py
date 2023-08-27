from playwright.async_api import async_playwright
# * ---
from constants import BASE_URL, PAGE_ACTIVE_COUPONS, ZUMUB_DATA_PATH
from scrape.interceptors import Interceptor
from scrape.models_playwright import Browser, Context, Action
from utils import Files
from scrape.zumub.utils.js_evaluate import JS_Evaluate
from scrape.zumub.products import Products
from database import Cache

class Coupons:
    @staticmethod
    async def get_async():
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)
                context = await Context(browser, BASE_URL).set_async()
                page = await context.new_page() 
                await page.route('**/*', Interceptor.block)
                await page.goto(f'{PAGE_ACTIVE_COUPONS}')
                await page.is_visible('voucher-info-wrapper')  
                coupons = await page.evaluate(JS_Evaluate.get_coupons())
                await Action.close_async(browser, context) 
            
            return coupons
        except Exception as e:
            raise Exception(e)
    
    @staticmethod
    async def get_products_async(result, id):
        try:
            # TODO from result(coupons) get link from id
            link = ''
            # * get category name
            category = link[(link.rfind('/') + 1):]
            raise Exception('NOT IMPLEMENTED')
            cached = Cache.get_per_category(category, 1)
            if cached is None:
                result = await Products.get_async(link) 
                Cache.set_per_category(category, 1, result)
            return cached      
        except Exception as e:
            raise Exception(e)