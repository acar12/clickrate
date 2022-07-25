# clickrate

A classifier using Naive Bayes to figure out if
a headline may be clickbait or not.

## run website
> cd frontend
> npm run build
> cd ..
> uvicorn api.main:app --reload
After that go to 127.0.0.1:8000/index.html (or whatever the URL is).

## data
`headlines.csv` - Training data <br>
`headlines.csv` - Testing data <br>
`words.csv` - Word data

## accuracy
Run `python test_model.py -v` to see for yourself.<br>
Test 1 - 92%<br>
Test 2 - 86%
