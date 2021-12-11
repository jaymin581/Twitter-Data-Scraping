import tweepy
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
print "Username: "+ user.screen_name
print "Followers: " + str(user.followers_count)
#followersCursor = tweepy.Cursor(api.followers,id=user_name, count = 100)
#for follower in followersCursor.items():
for follower in tweepy.Cursor(api.followers, id=user_name, count = 200).items():
	try:
		print follower.name.encode("utf-8")
		
	except tweepy.TweepError:
		time.sleep(1000)
		continue

	except StopIteration:
		break


print "================================================================"


ct_friend = 0
for friend in tweepy.Cursor(api.friends, id=user_name, count = 200).items():
	try:
		print friend.screen_name
		ct_friend = ct_friend + 1
		
	
	except tweepy.TweepError:
		time.sleep(3)
		continue

	except StopIteration:
		break
print "count of friend: " + str(ct_friend)



       


plotly.offline.plot({
"data": [
    plotly.graph_objs.Bar(x=['Followers','Followings'], y=[str(user.followers_count), str(ct_friend)])
]
plotly.graph_objs.Bar,size = 11
})
