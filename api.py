import tweepy
def twitter_api(twitter_id):
    consumer_key = ""
    consumer_secret = ""
    access_token = ""
    access_token_secret = ""

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)

    #twitter_id="elonmusk"

    cursor = tweepy.Cursor(api.user_timeline, id=twitter_id, tweet_mode="extended").items(250)
    tweet_list=""
    for i in cursor:
        tweet_list+=i.full_text
    return tweet_list    

