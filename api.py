# run for debug:
# uvicorn api:app --reload
# for website:
# uvicorn api:app --workers 4

from starlite import Starlite, get
from clickrate import ClickbaitClassifier as Model

model = Model()

@get(path="/{word:str}")
def predict_clickbait(word: str) -> dict[str, float]:
    return {
        "clickbait": model.predict_clickbait(word)
    }

app = Starlite(route_handlers=[predict_clickbait])
