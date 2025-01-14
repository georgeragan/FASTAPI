from fastapi import FastAPI
from fastapi .middleware.cors import CORSMiddleware
import pickle
import json
from pydantic import BaseModel

app=FastAPI()

class model_input(BaseModel):
    age:int
    sex:int
    bmi:float
    children:int
    smoker:int
    region: int

model=pickle.load(open("insurance_model","rb"))

@app.post("/insurance_prediction")#When a client sends a POST request to this URL with the required input data, the prediction function is executed.

def prediction(input_parameters:model_input):
    input_dict=input_parameters.dict()
    age=input_dict["age"]    
    sex=input_dict["sex"]
    bmi=input_dict["bmi"]
    children=input_dict["children"]
    smoker=input_dict["smoker"]
    region=input_dict["region"]
    predictions=model.predict([[age,sex,bmi,children,smoker,region]])
    return {"prediction":predictions}
