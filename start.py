import asyncio
from playwright.async_api  import async_playwright
from models.login_selectors import Login
from enviroment import EMAIL, PASSWORD

async def handle_dialog(dialog):
    assert dialog.type == 'beforeunload'
    await dialog.dismiss()
    
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
                        headless=False, 
                        slow_mo=50
                        )
        
        page = await browser.new_page(
            base_url='https://www.zumub.com/EN/'
        )    
        await page.goto('')
        await Login().submit_async(page, EMAIL, PASSWORD)
        await browser.close()

 
asyncio.run(main())