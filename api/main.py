import asyncio
from fastapi import FastAPI, status, HTTPException
from uuid import UUID
# * ---
from logger import Log
from zumub import Products
from zumub.coupons import Coupons
from models_playwright import Action

Log.set_configuration()
app = FastAPI()

# ! http://127.0.0.1:8000/products/coupon/
@app.get('/products/coupon/{id}')
async def products_by_coupon(id: UUID):
    try:
        result = await Coupons.get_products_async(id)
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
        result = await Products.get_by_page_async(category, nr)    
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
        result = await Products.get_by_category_async(category)    
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


