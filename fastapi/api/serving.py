import numpy as np
import joblib

from fastapi import APIRouter
from api.model.model import IrisInput, IrisResponse

serving = APIRouter()

model = joblib.load('./model/Iris_model.pkl')

@app.get("/predict")
async def read_root():
    return {"Message": "Data를 Json 형식으로 넣어주세요"}


@serving.post('/predict', response_model=IrisResponse, status_code=200)
async def predict(iris_input: IrisInput):
    input_data = np.array(iris_input.to_list()).astype(int).reshape(1, -1)

    predict_result = dict()
    predict_result['species'] = model.predict(input_data)[0]

    return predict_result
