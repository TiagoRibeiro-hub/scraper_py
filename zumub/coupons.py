from playwright.async_api import async_playwright
# * ---
from constants import BASE_URL, PAGE_ACTIVE_COUPONS, ZUMUB_DATA_PATH
from interceptors.interceptors import Interceptor
from models_playwright import Browser, Context, Action
from utils_files import Files

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
                coupons = await page.evaluate("""() => {
                    const vouchers = document.querySelectorAll('.voucher-info-wrapper');
 
                    let coupons = [];
                    for (let i = 0; i < vouchers.length; i++) {
                        const el = vouchers[i];
                        coupons.push({
                                id: ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)),
                                end_date: el.querySelector('div.voucher-end-date').innerText,
                                title: el.querySelector('.voucher-title').innerText,
                                message: el.querySelector('div.voucher-message').innerText,
                                link: el.querySelector('.voucher-title a').getAttribute('href')
                            });                        
                    }
                    return coupons;
                    }""")
                await Action.close_async(browser, context) 
                return Files.write_json(f"{ZUMUB_DATA_PATH}coupons", 'w', coupons)
  
        except Exception as e:
            raise Exception(e)