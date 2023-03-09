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
            tweets.append([tweet.user.username, tweet.content, tweet.likeCount, tweet.replyCount, tweet.retweetCount, tweet.quoteCount])
    return tweets

def create_JSON(tweet):
    tweetJSON = {
        "username": tweet[0],
        "content": tweet[1],
        "likeCount": tweet[2],
        "replyCount": tweet[3],
        "retweetCount": tweet[4],
        "quoteCount": tweet[5]
    }
    return tweetJSON



    

