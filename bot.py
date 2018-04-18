import tweepy
import time
import json
from footballData import *
from secrets import *

##############################################################################
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#API instance
api = tweepy.API(auth)

##############################################################################

#Current supported teams by the bot
supportedTeams = ['tigres'] 


#Post weekly the supported teams next match
def postNextMatches():

	#List for avoiding the repetition of a match
	secondaryTeams = []

	for team in supportedTeams:
		if (not(team in secondaryTeams) and time.localtime().tm_wday == 1):

			api.update_status('{} plays against {} on {} at {}'.format(team.capitalize(), 
				teams[team]['nextMatch']['against'], 
				teams[team]['nextMatch']['date'], 
				teams[team]['nextMatch']['stadium']))

			secondaryTeams.append(teams[team]['nextMatch']['against'])
	return None


#Post weekly the supported leagues positions
def postLeaguePositions():
	pass
	return None


########################
#Main
postNextMatches()











		






