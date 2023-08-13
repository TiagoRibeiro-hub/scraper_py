from models_playwright.context import Context
from interceptors.interceptors import Interceptor
from constants import BASE_URL, PAGE_EQUALS
from logger import Log

class Product:   
    @staticmethod
    async def get_products_by_page(browser, url, nr, total_products_page: int):
        try:
            context = await Context(browser, BASE_URL).set_async()
            page = await context.new_page()
            await page.route('**/*', Interceptor.block)
            await page.goto(f'{url}')           
            if nr is None:
                await page.goto(f'{url}')
            else:
                await page.goto(f'{url}{PAGE_EQUALS}{nr}')
                
            await page.is_visible('div.inner-product-box')
            # products_boxes = await page.query_selector_all('div.inner-product-box')
                
            # products = []
            # count_sold_off = 0
            # for product_box in products_boxes:
            #     product = await product_box.evaluate(Product.__js_get_product())
            #     if product is None:
            #         count_sold_off += 1 
            #     else:   
            #         products.append(product)
            #     if count_sold_off > 2:
            #         break
            #     total_products_page -= 1
            #     if total_products_page == 0:
            #         break
             
            products = await page.evaluate(Product.__js_get_products(), total_products_page) 
            await context.close()
            return products
        except Exception as e:
            Log.error('FUNC: GET_PRODUCTS_BY_PAGE', f'Somenthing went wrong, {e}')          
            raise Exception(e) 
        
    @staticmethod
    async def get_total_pages(browser, url) -> int:
        try:
            context = await Context(browser, BASE_URL).set_async()
            page = await context.new_page() 
            await page.route('**/*', Interceptor.block)
            await page.goto(f'{url}')
            await page.is_visible('div.pagination')   
            pagination = await page.query_selector('div.pagination p')
            total_pages = await pagination.evaluate(Product.__js_get_total_page())
            await context.close()
            return total_pages
        
        except Exception as e:
            Log.error('FUNC: TOTAL_PAGES', f'Somenthing went wrong, {e}')          
            raise Exception(e) 
    
    @staticmethod
    def __js_get_total_page() -> str:
        return """el => {
                    const total_products_page = el.children[1].innerText;
                    const total_products = el.children[2].innerText;
                    return {
                        total_products_page: total_products_page,
                        total_pages: Math.ceil(parseInt(total_products)/parseInt(total_products_page))
                        };
                }""" 
      
    @staticmethod  
    def __js_get_product() -> str:
        return """el => {
                if (el.querySelector('div.prod-image span.sold_discontinued') == null) {
                    const intro_anchor = el.querySelector("div.intro a");
                    const link = intro_anchor.getAttribute('href');
                    if (link) {
                        const has_coupon = el.querySelector('div.prod-image span.has_coupon');
                        const prices = el.querySelector('div.price-rate span');
                        let discount_price = "";
                        const has_discount = prices.querySelector('[class="strike"]');
                        if (has_discount != null) {
                            discount_price = has_discount.innerHTML;
                        }
                        let savings = "";
                        const has_savings_selector = prices.querySelector('[class="red"]');
                        if (has_savings_selector.children.length > 0) {
                            savings = has_savings_selector.innerText;
                        }
                        let couponDiscount = "";
                        if (has_coupon != null) {
                            couponDiscount = has_coupon.innerHTML;
                        }
                        const id = ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16))
                        return {
                            data_client: {
                                id: id,
                                name: intro_anchor.innerText, 
                                price: prices.querySelector('[class="real_price"]').innerText,
                                discount_price: discount_price,
                                savings: savings,
                                couponDiscount: couponDiscount
                            },
                            data_links: {
                                data_client_id: id,
                                link: link,
                            }
                        };                     
                    }
                };
                return null;
                }"""
    
    def __js_get_products() -> str:
        return """o => {
                    const all_products = document.querySelectorAll('div.inner-product-box');
                    data = [];
                    count_sold_discontinued = 0;
                    for (let i = 0; i < o.total_products_page; i++) {
                        const el = all_products[i];
                        if (el.querySelector('div.prod-image span.sold_discontinued') == null) {
                            const intro_anchor = el.querySelector("div.intro a");
                            const link = intro_anchor.getAttribute('href');
                            if (link) {
                                const has_coupon = el.querySelector('div.prod-image span.has_coupon');
                                const prices = el.querySelector('div.price-rate span');
                                let discount_price = "";
                                const has_discount = prices.querySelector('[class="strike"]');
                                if (has_discount != null) {
                                    discount_price = has_discount.innerHTML;
                                }
                                let savings = "";
                                const has_savings_selector = prices.querySelector('[class="red"]');
                                if (has_savings_selector.children.length > 0) {
                                    savings = has_savings_selector.innerText;
                                }
                                let couponDiscount = "";
                                if (has_coupon != null) {
                                    couponDiscount = has_coupon.innerHTML;
                                }
                                const id = ([1e7] + -1e3 + -4e3 + -8e3 + -1e11).replace(/[018]/g, c => (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16));
                                data.push({
                                    data_client: {
                                        id: id,
                                        name: intro_anchor.innerText,
                                        price: prices.querySelector('[class="real_price"]').innerText,
                                        discount_price: discount_price,
                                        savings: savings,
                                        couponDiscount: couponDiscount
                                    },
                                    data_links: {
                                        data_client_id: id,
                                        link: link,
                                    }
                                });
                            }
                        }
                        else {
                            count_sold_discontinued += 1;
                            if (count_sold_discontinued == 2) {
                                break;
                            }
                        }
                    };
                    return data;
                }"""