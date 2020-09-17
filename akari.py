import twitter
import tweepy
import time
import random
import os
from os import environ

consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']

key = environ['key']
secret = environ['secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)
api2 = tweepy.API(auth)
api = twitter.Api(consumer_key= consumer_key, consumer_secret= consumer_secret, access_token_key = key, access_token_secret = secret)

def postAkari():
    medialist = [api.UploadMediaChunked(media = 'AkariBraincells.mp4', additional_owners = None)]
    api2.update_status(status = '', media_ids = medialist)

while True:
    random24Hours = random.randint(1, 43200)
    postAkari()
    time.sleep(43200 + random24Hours)
