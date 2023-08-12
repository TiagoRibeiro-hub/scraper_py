from fastapi import FastAPI, status, HTTPException
from models_playwright import Action
# * ---
from zumub import Products
from logger import Log

Log.set_configuration()
app = FastAPI()

# ! http://127.0.0.1:8000/products/gallo
@app.get('/products/{product}')
async def products_by_brand(product: str):
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


