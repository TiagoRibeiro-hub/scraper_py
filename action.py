from enviroment import EMAIL, PASSWORD
from models_zumbu.login import Login
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from constants import BASE_URL, ZUMBU
from interceptors.interceptors import Interceptor

class Action:
    async def login_get_cookies_async(playwright):
        browser = await Browser.get_async(playwright, False)
        # * set context for login, get page, submit add get cookies
        context = await Context(browser, BASE_URL).set_async()    
        cookies = Cookies(context)            
        page = await context.new_page() 
        await page.route('**/*', Interceptor.block)
        page.on("request", Interceptor.request)
        page.on("response", Interceptor.response)
        await page.goto('')   
        await Login().submit_async(page, EMAIL, PASSWORD)
        await cookies.get_async()     
        await Action.close_async(browser, context)
             
    async def close_async(browser, context):
        await context.close()
        await browser.close()