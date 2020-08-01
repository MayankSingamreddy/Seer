# Seer

To run this (written for mac, commands should be similiar)


python3 -m venv env

source ./env/bin/activate

pip install spacy

python -m spacy download en_core_web_sm

pip install csv

pip install pandas

pip install textblob

pip install matplotlib



RedditCrawl can be reused for any new subreddit, just change the filename.csv in TextSent




IMPORTANT: ADDITIONAL USE CASES can be added by uncommenting at the bottom 




Reddit Seer that predicts the validity of user's predictions, as well as measuring the degree of a belief's radicalness.

Tool to scrape reddit comment text and compare user predictions of different entities against actualized data.
Keep track of accurate users, and connect to real data.
Huge implication: this is applicable to absolutely any subreddit which has some real life basis and isn’t self-contained

reddit/relationship_advice is overflowing with opinions about gender, which is data that can be compared to national abuse rates.
reddit/stocks makes daily predictions, all of which can be profited from.
One way or another, reddit is a mound of data waiting to be optimized.
Reddit Seer has infinite potential for thousands of use cases, including politics, video games, public markets, etc.

![Happy Christmas](Screen_Shot_2020-07-26_at_2.03.06_AM.png)
