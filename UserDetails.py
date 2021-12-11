import tweepy
import csv
import plotly
import plotly.graph_objs

consumer_key = "XXXXy4g4vOYRxUlY93lKRXXXX"
consumer_secret = "XXXXPvURFYzo69pW7VMST9bfXjDUhmFyMM0txnHTbjNbDmXXXX"
access_token = "XXXX858236-S6UGoyiD6VPBeLBxH93FuSZhdCcqCU2uXZsXXXX"
access_token_secret = "XXXX5JGaEaghpMKFApU7O7xv3jAVYfpaT9hGlQP4xXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user_name = raw_input("Please enter the Username: ")
user = api.get_user(user_name)


# def get_user_followDetails(user_name):
# def get_user_friends(user_name):
	

def get_all_tweets(screen_name):
	ct_follower = 0
	print "================= followers ================="
	for follower in tweepy.Cursor(api.followers, id=user_name, count = 200).items():
		try:
			
			print str(ct_follower) + " " + follower.name.encode("utf-8")
			ct_follower = ct_follower + 1
		
		except tweepy.TweepError:
			time.sleep(1000)
			continue

		except StopIteration:
			break
		
	print "count of followers: " + str(ct_follower)

	ct_friend = 0
	print "============ Followings / friends ============="
	for friend in tweepy.Cursor(api.friends, id=user_name, count = 200).items():
		try:
			
			print str(ct_friend) + " " + friend.screen_name
			ct_friend = ct_friend + 1
		
	
		except tweepy.TweepError:
			time.sleep(3)
			continue
		except StopIteration:
			break
	
	print "count of friend: " + str(ct_friend)

	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	# Array to contains the tweets
	alltweets = []	
	
	# Most Recent 100 Tweets
	new_tweets = api.user_timeline(screen_name = screen_name,count=100)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))

	
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.coordinates] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text", "Coordinates"])
		writer.writerows(outtweets)
		plotly.offline.plot({"data": [plotly.graph_objs.Bar(x=['Tweets', 'Followers','Followings'], y=[str(len(alltweets)), \
			str(user.followers_count), str(ct_friend)])]
		})
	
	pass


	



if __name__ == '__main__':
	#username of the account you want to download
	
	
	try:
		get_all_tweets(user_name)
	except tweepy.TweepError as e:
		print e.message + " It seems like User added privacy"
	
	#get_user_followDetails(user_name)
	#get_user_friends(user_name)

	

	#bar_chart(user_name)