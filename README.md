# clickrate

A classifier using Naive Bayes to figure out if
a headline may be clickbait or not.
[How does it work?](HOWITWORKS.md)

## run website
`cd frontend` <br>
`npm run build` <br>
`cd ..` <br>
`uvicorn api.main:app --reload` <br>
After that go to 127.0.0.1:8000/index.html (or whatever the URL is).

## data
`headlines.csv` - Training data <br>
`headlines.csv` - Testing data <br>
`words.csv` - Word data

## accuracy
Run `python test_model.py -v` to see for yourself.<br>
Test 1 - 92%<br>
Test 2 - 86%

## some model issues
- only 2 sources for news used to scrape
