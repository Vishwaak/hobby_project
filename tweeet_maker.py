import tweepy
from keys import *
try:
	security = tweepy.OAuthHandler(ck,csk)
	security.set_access_token(at,ats)
	me = tweepy.API(security)
except error:
	print("Error caught")	
inp = input("Enter the message you want to tweet : ")
me.update_status(inp)
print("I am done")
