"""
Basic API just so apps can use the model.
"""

from fastapi import FastAPI
from clickrate import ClickbaitClassifier

app = FastAPI()
model = ClickbaitClassifier()

@app.route("/{text}")
async def get_accuracy(text: str) -> float:
    return {"accuracy": model.predict_clickbait(text)}
