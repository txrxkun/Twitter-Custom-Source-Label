import tweepy
keys = dict(
consumer_key='PUT_YOUR_CONSUMER_KEY_HERE',
consumer_secret='PUT_YOUR_SECRET_KEY_HERE',
access_token='PUT_YOUR_ACCESS_TOKEN_HERE', 
access_token_secret='PUT_YOUR_ACCESS_TOKEN_SECRET_HERE'
)

user = "@YOURUSERNAME"

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

def tweet():
	message=input("Masukkan tweet anda lalu enter : ")
	api.update_status(message)
	time.sleep(1000)
if __name__ == "__main__":
	while 1:
		tweet()
