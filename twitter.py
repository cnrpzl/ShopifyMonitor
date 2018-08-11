import tweepy

def sendtotwitter(tweet):
    try:
        ckey = ""
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''
        auth = tweepy.OAuthHandler(ckey, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        user = api.me()
        api.update_status(status=tweet)
        print("Tweeted")
        return True
    except:
        return False
