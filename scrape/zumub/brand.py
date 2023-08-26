import json
from playwright.async_api import async_playwright
# * ---
from scrape.models_playwright import Browser, Context, Action
from scrape.interceptors import Interceptor
from scrape.zumub.utils.js_evaluate import JS_Evaluate
from constants import BASE_URL, PAGE_BRANDS, ZUMUB_DATA_PATH
from logger import Log
from utils import Files

class Brand:
    @staticmethod
    async def search_async(letter: str):
        try:
            async with async_playwright() as p:
                browser = await Browser.get_async(p, True)  
                context = await Context(browser, BASE_URL).set_async()
                page = await context.new_page()   
                await page.route('**/*', Interceptor.block) 
                await page.goto(f'{PAGE_BRANDS}')
             
                filter = f'#filter{letter.upper()}'
                await page.is_visible(f'{filter}')
                
                search_brands = await page.evaluate(JS_Evaluate.search_brand(), f'{filter}') 
                await Action.close_async(browser, context)
        
            return Files.write_json(f"{ZUMUB_DATA_PATH}search_brands", 'w', search_brands)
        except Exception as e:
            Log.error('FUNC: BRANDS_SEARCH_ASYNC', f'Somenthing went wrong, {e}')          
            raise Exception(e) 
