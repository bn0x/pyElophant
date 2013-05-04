"""
Import our modules 
"""

import urllib2
import urllib
import json

"""
Make sure to put in your API Key
"""
apiKey = 'Your API Key'

"""
The function to get summoner stats and return them.
'fail' is the only way to detect if an exception occured until I find another way.
"""

def summonerStats(region, requestData):
	try:
		if ' ' in requestData:
			requestData = requestData.replace(' ', '%20')
		apiURL = 'http://api.elophant.com/v2/' + region + '/' + 'summoner' + '/' + requestData + '?key=' + apiKey
		summonerURLOpen = urllib2.urlopen(apiURL)
		summonerJSON = json.load(summonerURLOpen)
		return { 'summonerLevel': summonerJSON['data']['summonerLevel'], 'name': summonerJSON['data']['name'], 'internalName': summonerJSON['data']['internalName'], 'revisionDate': summonerJSON['data']['revisionDate'], 'profileIconId': summonerJSON['data']['profileIconId'], 'acctId': summonerJSON['data']['acctId'], 'summonerId': summonerJSON['data']['summonerId'] }
	except:
		return { 'fail': 'Failed to get summoner stats.' }

def summonerLeagues(region, summonerName):
		try:
			if ' ' in summonerName:
				summonerName = summonerName.replace(' ', '%20')
			apiURL = 'http://api.elophant.com/v2/' + region + '/' + 'summoner' + '/' + summonerName + '?key=' + apiKey
			summonerURLOpen = urllib2.urlopen(apiURL)
			summonerJSON = json.load(summonerURLOpen)
			summonerID = summonerJSON['data']['summonerId']
			leagueURL = 'http://api.elophant.com/v2/' + region + '/' + 'leagues' + '/' + str(summonerID) + '?key=' + apiKey
			leagueURLOpen = urllib2.urlopen(leagueURL)
			leagueJSON = json.load(leagueURLOpen)
			tier = leagueJSON['data']['summonerLeagues'][0]['tier']
			league = leagueJSON['data']['summonerLeagues'][0]['name']
			playerOrTeamName = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['playerOrTeamName']
			requestorsRank = leagueJSON['data']['summonerLeagues'][0]['requestorsRank']
			return { 'requestorsRank': requestorsRank, 'summonerName': summonerName, 'tier': tier, 'league': league, 'rank': rank }
		except:
			return { 'fail': 'User is NOT ranked or an error has occured.' }