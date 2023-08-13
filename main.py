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

# ! http://127.0.0.1:8000/products/gallo
@app.get('/products/{product}')
async def products(product: str):
    try:
        result = await Products.get_async(product)
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


