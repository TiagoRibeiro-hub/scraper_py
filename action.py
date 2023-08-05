import asyncio
from enviroment import EMAIL, PASSWORD
from models_zumbu.login import Login
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from constants import BASE_URL
from logger.logger import Logger

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
    await close_async(browser, context)
            
async def close_async(browser, context):
    await context.close()
    await browser.close()
    
def cancel_all_tasks(exception):
    Logger.warning('cancel_all_tasks', f'A task failed with: {exception}, canceling all tasks')
    tasks  = asyncio.all_tasks()
    current = asyncio.current_task()
    tasks.remove(current)
    for task in tasks:
        task.cancel()