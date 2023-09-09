from .cache.products_cache import CacheProducts, ProductDto
from .cache.categories_cache import CacheCategories, CategoryDto

__all__ =[
    'CacheProducts', 'ProductDto',
    'CacheCategories', 'CategoryDto',
    ]



# class CouponsDto(JsonModel):
#     title: str
#     end_date: str
#     message: str
#     link: str
    
    
# class Pagination(JsonModel):
#     total: int
#     total_per_page: int
#     page_nr: Optional[int]