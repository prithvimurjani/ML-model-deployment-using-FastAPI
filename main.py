# -*- coding: utf-8 -*-

# 1. Importing libraries
import uvicorn #ASGI
from fastapi import FastAPI

# 2. Create the app object
app = FastAPI()

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, world'}

# 4. Route with a single parameter, returns the parameter within a message
# Located at http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name : str):
    return {'Welcome to my local webpage ': f'{name}'}

# 5. Run the API with uvicorn
# Will run on http://127.0.0.1:8000
    if __name__ == 'main':
        uvicorn.run(app, host='127.0.0.1', port = 8000) # in order to run asgi we use uvicorn.()
# uvicorn main:app --reload