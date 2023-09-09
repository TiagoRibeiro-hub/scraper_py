# * ---
from .cache import Cache
from logger import Log

from pydantic import BaseModel
from IndexedRedis import (
    IndexedRedisModel, 
    IRField,
    )

class ProductDto(BaseModel):
    id: int
    category: str
    page_nr: int
    name: str
    price: str
    discount_price: str
    savings: str
    coupon_discount: str
    link: str

class ProductDtoRedis(IndexedRedisModel):
	FIELDS = [ 
		IRField('category'),
		IRField('page_nr', valueType=int),
		IRField('name'),
		IRField('price'),
		IRField('discount_price'),
		IRField('savings'),
		IRField('coupon_discount'),
        IRField('link'),
	]

	INDEXED_FIELDS = [
        'category',
        'page_nr',
        'name',
	]

	KEY_NAME = 'ProductDtoRedis'
 
class CacheProducts:   
    @staticmethod
    def set_products(result , category, page_nr: int):
        Cache.connect()  
        try:
            products = []
            for product in result:
                product['category'] = category
                product['page_nr'] = page_nr
                new_product = ProductDtoRedis(
                   category= product['category'],
                   page_nr= product['page_nr'],
                   name= product['name'],
                   price= product['price'],
                   discount_price= product['discount_price'],
                   savings= product['savings'],
                   coupon_discount= product['coupon_discount'],
                   link= product['link'],
                )
                new_product.save()
                products.append(
                    ProductDto(
                        category= product['category'],
                        page_nr= product['page_nr'],
                        name= product['name'],
                        price= product['price'],
                        discount_price= product['discount_price'],
                        savings= product['savings'],
                        coupon_discount= product['coupon_discount'],
                        link= product['link'],
                        id = new_product.getPk(),
                    )
                )
                
            return products
        except Exception as e:
            Log.error("CACHE: SET_PRODUCTS", e)
    
    @staticmethod
    def find_all_products(category, page_nr):
        try:
            Cache.connect()        
            result = ProductDtoRedis.objects.filter(category=category).filter(page_nr=page_nr).all()
            products = []
            for product in result:
                products.append(
                    ProductDto(
                        category = product.category,
                        page_nr = product.page_nr,
                        name = product.name,
                        price = product.price,
                        discount_price = product.discount_price,
                        savings = product.savings,
                        coupon_discount = product.coupon_discount,
                        link = product.link,
                        id = product._id,
                    )
                )
            return products
            
        except Exception as e:
            Log.warning("CACHE: FIND_ALL_PRODUCTS", e)
            raise Exception(e)