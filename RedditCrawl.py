#test save
import praw
reddit = praw.Reddit(client_id= 'aQsnfnQKzpl9ng',
                     client_secret= 'rr5O0PUyyZDs8_Of1UgW5Q95Zzg',
                     user_agent='Reddit WebScraping')

import pandas as pd

comments = []
nba_subreddit = reddit.subreddit('nba')
#top 20 posts from the nba subreddit in the past week
for post in nba_subreddit.top("week", limit=20):
    post.comment_sort = 'top'
    post_comments = post.comments
    x = 0
    #cycles through top 20 comments
    for c in post_comments:
        top_comment = post_comments[x]
        #adds author, upvotes, and body of each comment to list
        comments.append([top_comment.author, top_comment.score, top_comment.body])
        x += 1
        if x == 20:
            break
comments = pd.DataFrame(comments,columns=['author', 'upvotes', 'body'])

#saves top 100 nba subreddit posts to csv file
comments.to_csv('\Users\MayankSingamreddy\Documents\SubredditSeer\nba_subreddit_comments.csv', index=False)
