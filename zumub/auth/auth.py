from playwright.async_api import async_playwright
import asyncio
from zumub.constants import BASE_URL
from enviroment import EMAIL, PASSWORD
import models_playwright.action as action  
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from logger.logger import Logger
from zumub.auth.models.login import Login

async def main():
    async with async_playwright() as p:   
        try:
            Logger.set_configuration_logger()
            browser = await Browser.get_async(p, False)
            # * set context for login, get page, submit add get cookies
            context = await Context(browser, BASE_URL).set_async()    
            cookies = Cookies(context)            
            page = await context.new_page() 
            await page.route('**/*', Interceptor.block)
            # page.on("request", Interceptor.request)
            # page.on("response", Interceptor.response)
            await page.goto('')   
            await Login().submit_async(page, EMAIL, PASSWORD)
            await cookies.get_async()     
            await action.close_async(browser, context)
            
        except Exception as e:
            action.cancel_all_tasks(e)
                 
asyncio.run(main())