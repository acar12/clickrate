"""
Basic API just so apps can use the model.
"""

from fastapi import FastAPI
from model import ClickbaitClassifier

app = FastAPI()
model = ClickbaitClassifier()

@app.get("/{text}")
async def get_accuracy(text: str) -> float:
    return {"clickbait": model.predict_clickbait(text)}
