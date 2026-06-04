from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from predictor import SentimentPredictor

class TextRequest(BaseModel):
    text: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = SentimentPredictor()

@app.post('/predict')
async def get_prediction(request: TextRequest):
    result = await model.predict(request.text)
    return result
    
if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
