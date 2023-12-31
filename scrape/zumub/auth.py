from playwright.async_api import async_playwright
# * ---
from constants import BASE_URL, ZUMUB_COOKIES_PATH
from enviroment import ZUMUB_EMAIL, ZUMUB_PASSWORD
from scrape.models_playwright import Action, Cookies, Browser, Context
from scrape.interceptors import Interceptor
from scrape.zumub.utils.login import Login

class Auth:
    async def login_async():
        try:
            async with async_playwright() as p:          
                browser = await Browser.get_async(p, False)
                # * set context for login, get page, submit add get cookies
                context = await Context(browser, BASE_URL).set_async()    
                cookies = Cookies(context, ZUMUB_COOKIES_PATH)            
                page = await context.new_page() 
                await page.route('**/*', Interceptor.block)
                # page.on("request", Interceptor.request)
                # page.on("response", Interceptor.response)
                await page.goto('')   
                await Login().submit_async(page, ZUMUB_EMAIL, ZUMUB_PASSWORD)
                await cookies.get_async()     
                await Action.close_async(browser, context)
        except Exception as e:
            Action.cancel_all_tasks(e)