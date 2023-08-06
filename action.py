import asyncio
from enviroment import EMAIL, PASSWORD
from models_zumbu.login import Login
from models_playwright.cookies import Cookies
from models_playwright.browser import Browser
from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from constants import BASE_URL, PAGE_EQUALS, ZUMBU
from logger.logger import Logger
from models_zumbu.product import Product

async def get_products(products_boxes, products):
    count_sold_off = 0
    for product_box in products_boxes:
        product = await product_box.evaluate(Product.get_product_js()) 
        if product is None:
            count_sold_off += 1 
        else:   
            products.append(product)
        if count_sold_off > 3:
            break
    return products

async def total_pages(page) -> int:
    try:
        await page.is_visible('div.pagination')   
        pagination = await page.query_selector('div.pagination p')
        return await pagination.evaluate("""el => {
                const total_products_page = el.children[1].innerText;
                const total_products = el.children[2].innerText;
                return Math.ceil(parseInt(total_products)/parseInt(total_products_page));
            }""")
    except Exception as e:
        Logger.error('FUNC: TOTAL_PAGES', f'Somenthing went wrong, {e}')          
        raise Exception(e)
    
async def get_products_by_page(browser, nr):
    context = await Context(browser, BASE_URL).set_async()
    page = await context.new_page()
    await page.goto(f'{ZUMBU}{PAGE_EQUALS}{nr}')  
    await page.is_visible('div.inner-product-box')  
    products_boxes = await page.query_selector_all('div.inner-product-box')
    products = []
    count_sold_off = 0
    for product_box in products_boxes:
        product = await product_box.evaluate(Product.get_product_js()) 
        if product is None:
            count_sold_off += 1 
        else:   
            products.append(product)
        if count_sold_off > 2:
            break
    await context.close()
    return products
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