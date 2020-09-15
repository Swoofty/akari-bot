import twitter
import tweepy
import time
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

media = api.UploadMediaChunked(media = 'AkariBraincells.mp4', additional_owners = None)
medialist = [media]
media0 = api.UploadMediaChunked(media = 'AkariBraincells.mp4', additional_owners = None)
medialist0 = [media0]

def postAkari(medialist):
    api2.update_status(status = '', media_ids = medialist)


while True:
    postAkari(medialist)
    time.sleep(10)
    postAkari(medialist0)
    time.sleep(10)