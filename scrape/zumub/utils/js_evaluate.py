class JS_Evaluate:
    @staticmethod
    def get_coupons() -> str:
        return """() => {
                    const vouchers = document.querySelectorAll('.voucher-info-wrapper');
                    let coupons = [];
                    for (let i = 0; i < vouchers.length; i++) {
                        const el = vouchers[i];
                        const has_link = el.querySelector('.voucher-title a');
                        link = '';
                        if (has_link) {
                            link = has_link.getAttribute('href')
                        }
                        coupons.push({
                                end_date: el.querySelector('div.voucher-end-date').innerText,
                                title: el.querySelector('.voucher-title').innerText,
                                message: el.querySelector('div.voucher-message').innerText,
                                link: link
                            });                        
                    }
                    return coupons;
                    }"""
    
    @staticmethod
    def get_total_page() -> str:
        return """el => {
                    const total_products_page = el.children[1].innerText;
                    const total_products = el.children[2].innerText;
                    return {
                        total_products_page: total_products_page,
                        total_pages: Math.ceil(parseInt(total_products)/parseInt(total_products_page))
                        };
                }""" 
      
    @staticmethod
    def get_products() -> str:
        return """() => {
            try {
                    const all_products = document.querySelectorAll('div.inner-product-box');
                    let data = [];
                    let count_sold_discontinued = 0;
                    const total = all_products.length / 2
                    
                    for (let i = 0; i < total; i++) {
                        const el = all_products[i];
                        if (el.querySelector('div.prod-image span.sold_discontinued') == null) {
                            const intro_anchor = el.querySelector("div.intro a");
                            const link = intro_anchor.getAttribute('href');
                            if (link) {                               
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
                                const has_coupon = el.querySelector('div.prod-image span.has_coupon');
                                let couponDiscount = "";
                                if (has_coupon != null) {
                                    couponDiscount = has_coupon.innerHTML;
                                }
                                data.push({
                                        name: intro_anchor.innerText,
                                        price: prices.querySelector('[class="real_price"]').innerText,
                                        discount_price: discount_price,
                                        savings: savings,
                                        coupon_discount: couponDiscount,
                                        link: link
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
            } catch (error) {
                return error
            }
                }"""
    
    @staticmethod
    def get_categories() -> str:
        return """
                () => {
                    var ul_childs = document.querySelector('ul.dropdown-menu.catagories.multi-level').children;
                    const categories = [];
                    for (let i = 0; i < ul_childs.length; i++) {
                        const li = ul_childs[i];
                        const a_link = li.querySelector('a');
                        const category = {
                            'name': a_link.innerText,
                            'sub_categories': []
                        }
                        const sub_ul_childs = li.querySelector('ul').children;
                        for (let j = 0; j < sub_ul_childs.length; j++) {
                            const sub_li = sub_ul_childs[j];
                            const sub_a_link = sub_li.querySelector('a');
                            category['sub_categories'].push({
                                'name': sub_a_link.innerText,
                                'link': sub_a_link.getAttribute('href'),
                            });
                        }
                        categories.push(category);
                    }  
                    return categories;  
                }"""
                
    @staticmethod
    def search_brand() -> str:
        return """
            filter => {
                const values = document.querySelector(filter).children[1].children;
                const brands = []
                for (let i = 0; i < values.length; i++) {
                    const value = values[i];
                    brands.push({
                        'name': value.innerText,
                        'link': value.querySelector('a').getAttribute('href')
                    });
                }
                return brands;
            }"""