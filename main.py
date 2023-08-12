from fastapi import FastAPI
from models_playwright import Action
# * ---
from zumub import Products
from logger import Log

Log.set_configuration()
app = FastAPI()

# ! http://127.0.0.1:8000/products/
@app.get("/products/{brand}")
async def products_by_brand(brand):
    try:
        return await Products.get_async(brand)
    except Exception as e:
        Action.cancel_all_tasks(e)

@app.get("/products/{product}")
async def products_by_product(product):
    try:
        return await Products.get_async(product)
    except Exception as e:
        Action.cancel_all_tasks(e)

