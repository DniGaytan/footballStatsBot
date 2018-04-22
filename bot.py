import tweepy
import time
import leagueData, teamData
from secrets import *

##############################################################################

def postNextMatches():
	"Post weekly the supported teams next match"
	for league in leagueData.leagues:
		tweet = ""
		for teamIndex in leagueData.leagues[league]:
			print(tweet)
			

	api.update_status(message)



			



###############################################################################

if __name__ == '__main__':
    # Constructs Twitter API instance
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)

    print(leagueData.leagues['ligaMX'])

    #postNextMatches()










		






