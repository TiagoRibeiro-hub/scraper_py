from playwright.async_api import async_playwright
# * ---
from constants import BASE_URL, PAGE_ACTIVE_COUPONS, ZUMUB_DATA_PATH
from interceptors.interceptors import Interceptor
from models_playwright import Browser, Context, Action
from utils import Files
from zumub.utils.js_evaluate import JS_Evaluate
from .products import Products

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
                return Files.write_json(f"{ZUMUB_DATA_PATH}coupons", 'w', coupons)
        except Exception as e:
            raise Exception(e)
    
    @staticmethod
    async def get_products_async(id):
        try:
            # TODO get link from id
            link = 'https://www.zumub.com/EN/sports-nutrition'
            return await Products.get_products_async(link)      
        except Exception as e:
            raise Exception(e)