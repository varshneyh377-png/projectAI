from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib
import numpy as np

class InputData(BaseModel):
    x1:float
    x2:float
    x3:float
    x4:float
    x5:float
#http://localhost:8000/docs 

scaler = joblib.load('Scaler.pkl')
model = joblib.load('model.pkl')
app=FastAPI()

@app.get('/')
def home():
    return {'message': 'Machine Learning API is running'}

@app.post('/predict/')
def predict(data:InputData):
    input_data = np.array([[data.x1, data.x2, data.x3, data.x4, data.x5]])
    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)
    prediction=int(prediction[0])
    return {'prediction': prediction}
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1',port=8000)
