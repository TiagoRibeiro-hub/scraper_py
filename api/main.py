from fastapi import FastAPI, status, HTTPException
from uuid import UUID
# * ---
from logger import Log
from scrape.zumub import Products, Coupons, Categories, Brand
from scrape.models_playwright import Action
from database import CacheProducts, ProductDto, CacheCategories, CategoryDto

Log.set_configuration()
app = FastAPI()

# ! http://127.0.0.1:8000/products/coupon/
@app.get('/products/coupon/{id}')
async def products_by_coupon(id: UUID):
    try:
        # TODO
        result = await Coupons.get_async()       
        result = await Coupons.get_products_async(result, id)

        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Not Found'
                )
        
        return result
    except Exception as e:
        Action.cancel_all_tasks(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}'
                ) 

# ! http://127.0.0.1:8000/products/protein/2
@app.get('/products/{category}/{nr}')
async def products(category: str, nr: int):
    try:    
        products = CacheProducts.find_all(category, 1)
        if len(products) == 0:
            result = await Products.get_by_page_async(category, nr)    
            products = CacheProducts.set(result, category, 1)     
    
        if not products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Not Found'
                )
        
        return result
    except Exception as e:
        Action.cancel_all_tasks(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}'
                )
        
# ! http://127.0.0.1:8000/products/gallo
@app.get('/products/{category}')
async def products(category: str) -> list[ProductDto]:
    try:
        products = CacheProducts.find_all(category, 1)
        if len(products) == 0:
            result = await Products.get_by_category_async(category)  
            products = CacheProducts.set(result, category, 1)
            
        if not products:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Not Found'
                )    
                
        return products
    
    except Exception as e:
        Action.cancel_all_tasks(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}'
                )
                   
# ! http://127.0.0.1:8000/products/coupons
@app.get('/coupons')
async def coupons():
    try:
        result = await Coupons.get_async()
            
        if not result:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Not Found'
                )
        
        return result
    except Exception as e:
        Action.cancel_all_tasks(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}'
                )

# ! http://127.0.0.1:8000/categories
@app.get('/categories')
async def categories() -> list[CategoryDto]:
    try:
        categories = CacheCategories.find_all()
        if len(categories) == 0:
            result = await Categories.get_async()
            categories = CacheCategories.set(result)
        
        if not categories:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Not Found'
                )
        
        return categories
    except Exception as e:
        Action.cancel_all_tasks(e)
        raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f'{e}'
                )

# ! http://127.0.0.1:8000/brands/s
@app.get('/searchbrands/{letter}')
async def search_brands(letter: str):
        try:
            # TODO CACHE
            result = await Brand.search_async(letter)
            if not result:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f'Not Found'
                    )
            
            return result
        except Exception as e:
            Action.cancel_all_tasks(e)
            raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail=f'{e}'
                    )