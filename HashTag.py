#Fetch all twits related which includes specific hashtags
import tweepy
import csv

consumer_key = "XXXXy4g4vOYRxUlY93lKRXXXX"
consumer_secret = "XXXXPvURFYzo69pW7VMST9bfXjDUhmFyMM0txnHTbjNbDmXXXX"
access_token = "XXXX858236-S6UGoyiD6VPBeLBxH93FuSZhdCcqCU2uXZsXXXX"
access_token_secret = "XXXX5JGaEaghpMKFApU7O7xv3jAVYfpaT9hGlQP4xXXXX"

def get_all_tweets(screen_name):

	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	
	# Array to contains the tweets
	alltweets = []	
	
	# Most Recent 100 Tweets
	new_tweets = api.search("%23"+query, count=100)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	
	while len(new_tweets) > 0:
		print "we are getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.search("%23"+query, count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id, tweet.created_at, tweet.user.name, tweet.text.encode("utf-8"), str(tweet.source.encode("utf-8")), tweet.user.location, \
	tweet.coordinates] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at", "UserName", "text", "UserLocation", "Source", "Coordinates"])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#username of the account you want to download
	query = raw_input("HashTag: ")

	try:
		get_all_tweets(query)

	except tweepy.TweepError as e:
		print e.message + "Something Wrong"