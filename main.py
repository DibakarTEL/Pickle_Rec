from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
	text: int

class PredictionOut(BaseModel):
	recommendations: list


@app.get("/")
def home():
	return {"health_check": "OK", "model_version": model_version}

@app.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    recommendations = predict_pipeline(payload.text)
    return {"language": recommendations}