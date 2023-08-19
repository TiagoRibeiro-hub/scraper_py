from pydantic import BaseModel, HttpUrl
from uuid import UUID

class Product(BaseModel):
    id: UUID
    name: str
    price: float
    discount_price: float | None
    savings: str | None
    coupon_discount: str | None
    
class Links(BaseModel):
    link: HttpUrl
    fk_id: UUID
    
class Pagination(BaseModel):
    total: int
    total_per_page: int
    page_nr: int | None

class Coupons(BaseModel):
    id: UUID
    title: str
    end_date: str
    message: str