from fastapi import FastAPI

app = FastAPI()

proxy_db = {
        1: 'First item',
        2: 'Second item'
        }

@app.get('/')
async def index():
    return {'message': 'Hello world!'}

@app.get('/items/{item_id:int}')
async def items(item_id):
    return {
        "item_id": item_id,
        "item_val": proxy_db[item_id]
        }
