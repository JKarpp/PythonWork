#!/usr/bin/env python3
import tweepy

#Auth to twiter
#for the OAuthHandler use the API key followed by th API Secret Key 
auth = tweepy,OAuthHandler("","")
#for the set_access_token, use the access token followed by the access token secret
auth.set_access_token("","")
api = tweepy.API(auth)

if (api.verify_credentials()):
    print("Auth Ok")
else:
    print("Error during auth")

#Uncomment this line to add texts into tweets. This will post to your 
# twitter feed linked to the API keys
#api.update_status("")

#This block of code will allow you to read the recent tweets. 
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)