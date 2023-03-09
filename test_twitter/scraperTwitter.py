import snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
from datetime import datetime




tweets = []

def get_tweets(query, limit):
    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        if len(tweets) == limit :
            break
        else:
            tweets.append([tweet.user.username, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount, tweet.date])
        if len(tweets)<limit:
            print("Not enough tweets found, only " + str(len(tweets)) + " tweets found")
    return tweets

def create_JSON(tweet):
    tweetJSON = {
        "username": tweet[0],
        "content": tweet[1],
        "likeCount": tweet[2],
        "replyCount": tweet[3],
        "retweetCount": tweet[4],
        "quoteCount": tweet[5],
        "date": tweet[6].strftime("%Y-%m-%dT%H:%M:%S")
    }
    return tweetJSON



    
##test
##query = "astérix lang:fr"
##limit = 300
##tweets = get_tweets(query, limit)
print(len(tweets))
##for tweet in tweets:
    ##tweet = create_JSON(tweet)
    ##print(tweet)

