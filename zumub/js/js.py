def get_total_page() -> str:
    return """el => {
                const total_products_page = el.children[1].innerText;
                const total_products = el.children[2].innerText;
                return Math.ceil(parseInt(total_products)/parseInt(total_products_page));
            }""" 
            
def get_product() -> str:
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