import tweepy
import datetime
import time
from secrets import *

##############################################################################

def tweetNextMatch(requestedTeam):
	"""Retrieve the corrresponding data and tweet it || trigger : nextMatch [team], sigPartido [team]"""
	msgData = []
	data = ""

	#opens file for reading the #nextmatch data
	dataFile = open('data.txt', 'r+')
	#reads the first line of the data.txt
	line = dataFile.readline()

	while not '#nextmatch' in line:
		line = dataFile.readline()

	#reads the nextline just for start looking within the #nextmatch data
	line = dataFile.readline()

	#reads the whole bunch of info within #nextmatch
	while (not '#' in line):

		#looks for the requested team info if it exists
		if requestedTeam.lower() in line:
			for char in line:
				if char is "-":
					msgData.append(data)
					data = ""
				else:
					data += char
			api.update_status("{} vs {} at {} on {}".format(msgData[0].capitalize(), msgData[1].capitalize(), msgData[2].capitalize(), msgData[3]))
			break
		line = dataFile.readline()
	dataFile.close()


def tweetPastMatch(requestedTeam):
	"""Retrieve the corresponding data and tweet it  || trigger : pastMatch [team], pasPartido [team]"""
	msgData = []
	data = ""

	dataFile = open('data.txt', 'r+')
	line = dataFile.readline()

	while not '#pastmatch' in line:
		line = dataFile.readline()

	line = dataFile.readline()

	while (not '#' in line):
		#looks for the requested team info if it exists
		if requestedTeam.lower() in line:
			for char in line:
				if char is "-":
					msgData.append(data)
					data = ""
				else:
					data += char
			api.update_status("{} vs {} at {} on {}, and the result was {}".format(msgData[0].capitalize(), msgData[1].capitalize(), msgData[2].capitalize(), msgData[3], msgData[4]))
			break
		line = dataFile.readline()
	dataFile.close()



def checkMentions():
	"""Retrieve all the @SoccerbotStats mentions"""

	followers = api.followers()
	mentionTweets = []
	followersTLindex = {}

	for follower in followers:
		firstTweet = True
		for tweet in api.user_timeline(follower):
			if '@SoccerbotStats' in tweet.text:
				mentionTweets.append(tweet)
				if firstTweet:
					followersTLindex[tweet.screen_name] = tweet.id
					firstTweet = False

	return mentionTweets, followersTLindex


###############################################################################

if __name__ == '__main__':
    # Constructs Twitter API instance
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    
    mentionTweets, followersTLindex = checkMentions()

    







    













		






