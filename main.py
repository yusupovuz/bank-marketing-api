import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

model = joblib.load('bank_marketing.pkl')


class Data(BaseModel):
    age:int
    balance:int
    day:int
    duration:int
    campaign:int
    pdays:int
    previous:int
    job:str
    marital:str
    education:str
    default:str
    housing:str
    loan:str
    contact:str
    month:str


# @app.post('/predict')
# def predict(data:Data):
#     df = pd.DataFrame(data)
#     df = df.set_index(0).T
#     y_pred = model.predict(df)
#     print(y_pred)
#     return {
#         'Prediction':(y_pred[0])
#     }

@app.post('/predict')
def predict(data:Data):
    data_dict = data.model_dump()
    df = pd.DataFrame([data_dict])
    y_pred = model.predict(df)
    return {
        'Prediction':y_pred[0]
    }