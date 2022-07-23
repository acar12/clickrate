from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from clickrate import ClickbaitClassifier

model = ClickbaitClassifier()
app = FastAPI()

@app.get("/text/{text:str}")
async def predict_clickbait(text: str) -> JSONResponse:
    return {"percent_clickbait": model.predict_clickbait(text)}

app.mount("/", StaticFiles(directory="static"), name="static")
