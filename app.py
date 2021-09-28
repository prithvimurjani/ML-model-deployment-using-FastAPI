#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 22:48:47 2021

@author: acer
"""

# 1. Import libraries
import uvicorn
from fastapi import FastAPI
from InputModel import InputModel
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()
pickle_in = open("model_built_fapi.pkl", "rb")
regressor = pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, world'}

# 4. Route with a single parameter, returns the parameter within a message
# Located at http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name : str):
    return {'Welcome to my local webpage ': f'{name}'}


# 5. Predict the y value from the input x taken in JSON format to return the value for y as y = 2*x +1
@app.post('/predict')
def predict_yValue(data : InputModel):
    data = data.dict()
    print(data)
    x = data['xValue']
    print(x)
    prediction = regressor.predict([[x]])
    # Accessing first element as it returns as regressor.predict([[300]])
    return {
        'prediction' : 'The value of y is : {}'.format(prediction[0])
        }


# 5. Run the API with uvicorn
# Will run on http://127.0.0.1:8000
    if __name__ == 'main':
        uvicorn.run(app, host='127.0.0.1', port = 8000) # in order to run asgi we use uvicorn.()
# uvicorn app:app --reload