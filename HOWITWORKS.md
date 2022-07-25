# how it works
The model works by using the [Bayes Theorem](https://en.wikipedia.org/wiki/Bayes%27_theorem).<br>
![image](https://user-images.githubusercontent.com/39702495/180804565-b7a41b8b-1908-4d84-a33b-6a1258b698fb.png)<br>
Where `A` is the event that the headline is clickbait, and `B` is the event where the headline contains a certain word (which affects if it's clickbait or not).
`B` doesn't have to be just one word though, as there can be multiple `B` events for multiple words. The frequencies of these words are used as data for the model.

# simplified
The model uses data from known clickbait sources and non-clickbait sources so we know what words are used more often or not for clickbait.
So the model can then guess if the headline may be clickbait depending on the words it has in common with the clickbait and non-clickbait headlines.
[Dataset here](https://www.kaggle.com/datasets/amananandrai/clickbait-dataset).

The source code for the model is `clickrate/model.py`.
