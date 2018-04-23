import tweepy
import datetime
from secrets import *

##############################################################################

def tweetNextMatch(requestedTeam):
	"""Retrieve the corrresponding data and tweet it"""
	msgData = []
	data = ""

	#opens file for reading the #nextmatch data
	dataFile = open('data.txt', 'r+')
	#reads the first line of the data.txt
	line = dataFile.readline()

	while not '#nextmatch' in line:
		line = dataFile.readline()

	#reads the nextline just for start looking within the #nextmatch data
	line = datFile.readline()

	#reads the whole bunch of info within #nextmatch
	while (not '#' in line):

		#looks for the requested team info if it exists
		if requestedTeam.lower() in line:
			for char in line:
				if char is "-":
					msgData.append(data)
					data = ""
				data += char
			api.status_update("{} vs {} at {} on {}".format(msgData[0], msgData[1], msgData[2], msgData[3]))
			break
		line = dataFile.readline()
	dataFile.close()


def tweetPastMatch():
	"""Retrieve the corresponding data and tweet it"""
	msgData = []
	data = ""

	dataFile = open('data.txt', 'r+')
	line = dataFile.readline()

	while not '#pastmatch' in line:
		line = dataFile.readline()

	line = datFile.readline()

	while (not '#' in line):
		#looks for the requested team info if it exists
		if requestedTeam.lower() in line:
			for char in line:
				if char is "-":
					msgData.append(data)
					data = ""
				data += char
			api.status_update("{} vs {} at {} on {}, and the result was {}".format(msgData[0], msgData[1], msgData[2], msgData[3], msgData[4]))
			break
		line = dataFile.readline()
	dataFile.close()







			



###############################################################################

if __name__ == '__main__':
    # Constructs Twitter API instance
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    botTimeline = api.home_timeline()



    













		






