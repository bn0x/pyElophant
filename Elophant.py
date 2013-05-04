"""
Import our modules 
"""

import urllib2
import urllib
import json

"""
Make sure to put in your API Key
"""
apiKey = 'Put in your API key'

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
			rank = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['rank']
			previousDayLeaguePosition = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['previousDayLeaguePosition']
			hotStreak = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['hotStreak']
			freshBlood = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['freshBlood']
			lastPlayed = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['lastPlayed']
			playerOrTeamId = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['playerOrTeamId']
			inactive = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['inactive']
			veteran = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['veteran']
			queueType = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['queueType']
			losses = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['losses']
			playerOrTeamName = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['playerOrTeamName']
			wins = leagueJSON['data']['summonerLeagues'][0]['entries'][0]['wins']
			return { 'summonerName': summonerName, 'tier': tier, 'league': league, 'rank': rank, 'previousDayLeaguePosition': previousDayLeaguePosition, 'hotStreak': hotStreak, 'freshBlood': freshBlood, 'lastPlayed': lastPlayed, 'playerOrTeamId': playerOrTeamId, 'inactive': inactive, 'veteran': veteran, 'queueType': queueType, 'losses': losses, 'playerOrTeamName': playerOrTeamName, 'wins': wins }
		except:
			return { 'fail': 'User is NOT ranked or an error has occured.' }