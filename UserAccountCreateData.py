#Fetch twitter account creation date

import tweepy
import json


consumer_key = "XXXXy4g4vOYRxUlY93lKRXXXX"
consumer_secret = "XXXXPvURFYzo69pW7VMST9bfXjDUhmFyMM0txnHTbjNbDmXXXX"
access_token = "XXXX858236-S6UGoyiD6VPBeLBxH93FuSZhdCcqCU2uXZsXXXX"
access_token_secret = "XXXX5JGaEaghpMKFApU7O7xv3jAVYfpaT9hGlQP4xXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api = tweepy.API(auth_handler=auth, parser=tweepy.parsers.JSONParser())
user_name = raw_input("Enter Username to get the Account Creation date: ")
user_data = api.get_user(user_name)

AccountCreationDate = user_data["created_at"]
full_name = user_data["name"].encode('utf8')
#print user_data
print ":_______________________________________"
print "Account Created on: " + AccountCreationDate
print "Full Name: " + full_name
#print user_data["profile_location"]

      




