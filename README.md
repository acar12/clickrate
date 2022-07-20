# clickrate

A classifier using Naive Bayes to figure out if
a headline may be clickbait or not.

## data
`headlines.csv` - Training data <br>
`headlines.csv` - Testing data <br>
`words.csv` - Word data (run get_words.py)

## accuracy
Run `python test_model.py -v` to see for yourself.<br>
Test 1 - 92% (csv file)<br>
Test 2 - 87% (buzzfeed.com and apnews.com as of 7/19/2022)