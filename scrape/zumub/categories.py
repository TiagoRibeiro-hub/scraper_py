from playwright.async_api import async_playwright
# * ---
from scrape.models_playwright import Browser, Context, Action
from scrape.interceptors import Interceptor
from scrape.zumub.utils.js_evaluate import JS_Evaluate
from constants import BASE_URL
from logger import Log

class Categories:
    @staticmethod
    async def get_async():
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)  
                context = await Context(browser, BASE_URL).set_async()
                page = await context.new_page()   
                await page.route('**/*', Interceptor.block) 
                await page.goto('')
                await page.is_visible('li.dropdown.drop-nav')
                categories = await page.evaluate(JS_Evaluate.get_categories()) 
                await Action.close_async(browser, context)
        
            return categories
        except Exception as e:
            Log.error('FUNC: GET_CATEGORIES_ASYNC', f'Somenthing went wrong, {e}')          
            raise Exception(e) 

