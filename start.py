from playwright.async_api import async_playwright
import asyncio
# * ---
from logger import Log
from models_playwright import Action
import zumub as Zumub
from constants import BASE_URL, ZUMBU

# async def main():
#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         page = await browser.new_page()
#         await page.goto(f'{BASE_URL}{ZUMBU}')
#         products_boxes = await page.query_selector_all('div.inner-product-box')
#         products_boxes.
#         await page.close() 
           
    # try:
    #     Log.set_configuration()
    #     await Zumub.Auth.login_async()
    # except Exception as e:
    #     Action.cancel_all_tasks(e)

# asyncio.run(main())