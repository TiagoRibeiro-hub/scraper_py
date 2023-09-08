from typing import List, Optional
from pydantic import HttpUrl
from redis_om import JsonModel, Field, EmbeddedJsonModel

class ProductDto(JsonModel):
    name: str = Field(index=True, full_text_search=True)
    price: str = Field(index=True)
    discount_price: Optional[str]
    savings: Optional[str]
    coupon_discount: Optional[str]

class CouponsDto(JsonModel):
    title: str
    end_date: str
    message: str
    link: HttpUrl
    
class SubCategory(EmbeddedJsonModel):
    name: str = Field(index=True)
    link: HttpUrl
    
class Category(JsonModel):
    name: str = Field(index=True)
    link: HttpUrl
    sub_category: List[SubCategory]
    
    
# class Pagination(JsonModel):
#     total: int
#     total_per_page: int
#     page_nr: Optional[int]