class Product:
    def __init__(self, 
                 name, 
                 link, 
                 price, 
                 discount_price, 
                 savings, coupon_discount = None
                 ) -> None:
        self.name = name
        self.link = link
        self.price = price
        self.discount_price = discount_price
        self.savings = savings
        self.coupon_discount = coupon_discount
        
    @staticmethod
    def get_product_js() -> str:
        return """el => {
                if (el.querySelector('div.prod-image span.sold_discontinued') == null) {
                    const intro_anchor = el.querySelector("div.intro a");
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
                    return {
                        name: intro_anchor.innerText, 
                        link: intro_anchor.getAttribute('href'),
                        price: prices.querySelector('[class="real_price"]').innerText,
                        discount_price: discount_price,
                        savings: savings,
                        couponDiscount: couponDiscount
                    };
                };
                return null;
                }"""