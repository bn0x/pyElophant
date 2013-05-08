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
		
		apiURL = 'http://api.elophant.com/v2/%s/summoner/%s?key=%s' % (region, requestData, apiKey)
		summonerURLOpen = urllib2.urlopen(apiURL)
		summonerJSON = json.load(summonerURLOpen)
		
		return { 'summonerLevel': summonerJSON['data']['summonerLevel'], 'name': summonerJSON['data']['name'], 'internalName': summonerJSON['data']['internalName'], 'revisionDate': summonerJSON['data']['revisionDate'], 'profileIconId': summonerJSON['data']['profileIconId'], 'acctId': summonerJSON['data']['acctId'], 'summonerId': summonerJSON['data']['summonerId'] }
	
	except:
		return { 'fail': 'Failed to get summoner stats.' }

"""
Ranked stats
Plan on cleaning up the tier output maybe soon.
Currently only gets the requested users data.
Doing points and stuff on another day.
"""

def summonerLeagues(region, summonerName):
	try:
		if ' ' in summonerName:
			summonerName = summonerName.replace(' ', '%20')
		
		apiURL = 'http://api.elophant.com/v2/%s/summoner/%s?key=%s' % (region, summonerName, apiKey)
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

"""
Team 5v5 win/loss lookup
Rating isn't included as it seems broken on Elophant.

I'll eventually write in 3v3 and whatever the fuck ODIN means...
Roster too... as this is a libary and not just for my personal needs I guess.

I'm aware this if-else tree is ugly but I'm really bad at scripting/programming so if you use this just bear with it.
"""


def teamLookup(region, teamName):
	try:
		if ' ' in teamName:
			teamName = teamName.replace(' ', '%20')
		
		apiURL = 'http://api.elophant.com/v2/%s/find_team/%s?key=%s' % (region, teamName, apiKey)
		print apiURL
		teamURLOpen = urllib2.urlopen(apiURL)
		teamJSON = json.load(teamURLOpen)
		statDetails = teamJSON['data']['teamStatSummary']['teamStatDetails']

		wins5, losses5, wins3, losses3 = -1, -1, -1, -1
		
		for index in range(0, 3):
				if 'RANKED_TEAM_5x5' in statDetails[index]['teamStatType']:
					wins5 = statDetails[index]['wins']
					losses5 = statDetails[index]['losses']
					break

		for index in range(0, 3):
				if 'RANKED_TEAM_3x3' in statDetails[index]['teamStatType']:
					wins3 = statDetails[index]['wins']
					losses3 = statDetails[index]['losses']
					break

		if wins5 == -1:
			return { 'fail': 'Failed to find team\'s 5v5 ranked record.' }
		return { 'losses5': losses5, 'wins5': wins5, 'wins3': wins3, 'losses3': losses3 }

	except:
		return { 'fail': 'Failed to find team\'s 5v5 ranked record.' }