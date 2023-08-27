from fastapi import FastAPI, status, HTTPException
from uuid import UUID
# * ---
from logger import Log
from scrape.zumub import Products, Coupons, Categories, Brand
from scrape.models_playwright import Action
from database import Cache

Log.set_configuration()
Cache.connect()
app = FastAPI()

# ! http://127.0.0.1:8000/products/coupon/
@app.get('/products/coupon/{id}')
async def products_by_coupon(id: UUID):
    try:
        result = Cache.get('coupons')
        if result is None:
            result = await Coupons.get_async()
            Cache.set('coupons', result)
            
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
        result = Cache.get_per_category(category, nr)
        if result is None:
            result = await Products.get_by_page_async(category, nr)  
            Cache.set_per_category(category, nr, result)  
        
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
        
# ! http://127.0.0.1:8000/products/gallo
@app.get('/products/{category}')
async def products(category: str):
    try:
        result = Cache.get_per_category(category, 1)
        if result is None:
            result = await Products.get_by_category_async(category)  
            Cache.set_per_category(category, 1, result)
               
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
                   
# ! http://127.0.0.1:8000/products/coupons
@app.get('/coupons')
async def coupons():
    try:
        result = Cache.get('coupons')
        if result is None:
            result = await Coupons.get_async()
            Cache.set('coupons', result)
            
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
async def categories():
    try:
        result = Cache.get('categories')
        if result is None:
            result = await Categories.get_async()
            Cache.set('categories', result)
            
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