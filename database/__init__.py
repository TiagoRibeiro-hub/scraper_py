from .cache.products_cache import CacheProducts, ProductDto

__all__ =[
    'CacheProducts', 
    'ProductDto',
    ]



# class CouponsDto(JsonModel):
#     title: str
#     end_date: str
#     message: str
#     link: str
    
# class SubCategory(EmbeddedJsonModel):
#     name: str
#     link: str
    
# class Category(JsonModel):
#     name: str
#     sub_category: List[SubCategory]
    
    
# class Pagination(JsonModel):
#     total: int
#     total_per_page: int
#     page_nr: Optional[int]