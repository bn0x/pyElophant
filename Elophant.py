"""
Import our modules 
"""

import urllib2
import urllib
import json

"""
Make sure to put in your API Key
"""
apiKey = 'Your API key'

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
		
		return { 'summonerLevel': summonerJSON['data']['summonerLevel'],
				 'name': summonerJSON['data']['name'], 
				 'internalName': summonerJSON['data']['internalName'], 
				 'revisionDate': summonerJSON['data']['revisionDate'], 
				 'profileIconId': summonerJSON['data']['profileIconId'], 
				 'acctId': summonerJSON['data']['acctId'], 
				 'summonerId': summonerJSON['data']['summonerId'] }
	
	except:
		return { 'fail': 'Failed to get summoner stats.' }

"""
Ranked stats
Gets all members in requested users league and the requested users data
"""

def summonerLeagues(region, summonerName):
	try:
		if ' ' in summonerName:
			summonerName = summonerName.replace(' ', '%20')
		
		apiURL = 'http://api.elophant.com/v2/%s/summoner/%s?key=%s' % (region, summonerName, apiKey)
		summonerURLOpen = urllib2.urlopen(apiURL)
		summonerJSON = json.load(summonerURLOpen)
		
		summonerID = summonerJSON['data']['summonerId']
		leagueURL = 'http://api.elophant.com/v2/%s/leagues/%s?key=%s' % (region, str(summonerID), apiKey)
		leagueURLOpen = urllib2.urlopen(leagueURL)
		leagueJSON = json.load(leagueURLOpen)
		
		tier = leagueJSON['data']['summonerLeagues'][0]['tier']
		league = leagueJSON['data']['summonerLeagues'][0]['name']
		requestorsRank = leagueJSON['data']['summonerLeagues'][0]['requestorsRank']
		entries = leagueJSON['data']['summonerLeagues'][0]['entries']
		members = []
		previousDayLeaguePositions = []
		hotStreaks = []
		freshBloods = []
		tiers = []
		lastPlayeds = []
		playerOrTeamIds = []
		leaguePointss = []
		inactives = []
		ranks = []
		veterans = []
		queueTypes = []
		lossess = []
		playerOrTeamNames = []
		winss = []

		for index in range(0, len(entries)):
			member = entries['playerOrTeamName']
			previousDayLeaguePosition = entries['previousDayLeaguePosition']
			hotStreak = entries['hotStreak']
			freshBlood = entries['freshBlood']
			tier = entries['tier']
			lastPlayed = entries['lastPlayed']
			playerOrTeamId = entries['playerOrTeamId']
			leaguePoints = entries['leaguePoints']
			inactive = entries['inactive']
			rank = entries['rank']
			veteran = entries['veteran']
			queueType = entries['queueType']
			losses = entries['losses']
			playerOrTeamName = entries['playerOrTeamName']
			wins = entries['wins']
			members.append(member)
			previousDayLeaguePositions.append(previousDayLeaguePosition)
			hotStreaks.append(hotStreak)
			freshBloods.append(freshBlood)
			tiers.append(tier)
			lastPlayeds.append(lastPlayed)
			playerOrTeamIds.append(playerOrTeamId)
			leaguePointss.append(leaguePoints)
			inactives.append(inactive)
			ranks.append(rank)
			veterans.append(veteran)
			queueTypes.append(queueType)
			lossess.append(losses)
			playerOrTeamNames.append(playerOrTeamName)
			winss.append(wins)

		return { 'requestorsRank': requestorsRank,
				 'summonerName': summonerName,
				 'tier': tier,
				 'league': league,
				 'rank': rank,
				 'members': members[0:]
				 'previousDayLeaguePosition': previousDayLeaguePositions[0:],
				 'hotStreak': hotStreaks[0:],
				 'freshBlood': freshBloods[0:],
				 'tier': tiers[0:],
				 'lastPlayed': lastPlayeds[0:],
				 'playerOrTeamId': playerOrTeamIds[0:],
				 'leaguePoints': leaguePointss[0:],
				 'inactive': inactives[0:],
				 'rank': ranks[0:],
				 'veteran': veterans[0:],
				 'queueType': queueTypes[0:],
				 'losses': lossess[0:],
				 'playerOrTeamName': playerOrTeamNames[0:],
				 'wins': winss[0:] }
	
	except:
		return { 'fail': 'User is NOT ranked or an error has occured.' }

"""
Team 5v5 win/loss lookup
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
		teamRoster = teamJSON['data']['roster']
		players, joinDates, inviteDates, statusInTeam, playerIds = [], [], [], [], []
		wins5, losses5, wins3, losses3 = -1, -1, -1, -1
		
		for index in range(0, 3):
				if 'RANKED_TEAM_5x5' in statDetails[index]['teamStatType']:
					wins5 = statDetails[index]['wins']
					losses5 = statDetails[index]['losses']
					maxRating5 = statDetails[index]['maxRating']
					seedRating5 = statDetails[index]['seedRating']
					rating5 = statDetails[index]['rating']
					averageGamesPlayed5 = statDetails[index]['averageGamesPlayed']
					break

		for index in range(0, 3):
				if 'RANKED_TEAM_3x3' in statDetails[index]['teamStatType']:
					wins3 = statDetails[index]['wins']
					losses3 = statDetails[index]['losses']
					maxRating3 = statDetails[index]['maxRating']
					seedRating3 = statDetails[index]['seedRating']
					rating3 = statDetails[index]['rating']
					averageGamesPlayed3 = statDetails[index]['averageGamesPlayed']
					break

		for index in range(0, len(teamRoster['memberList'])):
				joinDate = teamRoster['memberList'][index]['joinDate']
				playerName = teamRoster['memberList'][index]['playerName']
				inviteDate = teamRoster['memberList'][index]['inviteDate']
				status = teamRoster['memberList'][index]['status']
				playerId = teamRoster['memberList'][index]['playerId']
				players.append(playerName)
				joinDates.append(joinDate)
				inviteDates.append(inviteDate)
				statusInTeam.append(status)
				playerIds.append(playerId)


		if wins5 == -1:
			return { 'fail': 'Failed to find team\'s ranked record.' }


		return { 'losses5': losses5,
				 'wins5': wins5,
				 'maxRating5': maxRating5,
				 'seedRating5': seedRating5,
				 'rating5': rating5,
				 'averageGamesPlayed5': averageGamesPlayed5,
				 
				 'wins3': wins3, 
				 'losses3': losses3, 
				 'maxRating3': maxRating3,
				 'seedRating3': seedRating3,
				 'rating3': rating3,
				 'averageGamesPlayed3': averageGamesPlayed3, 

				 'members': players[0:],
				 'joinDates': joinDates[0:],
				 'inviteDates': inviteDates[0:],
				 'statusInTeam': statusInTeam[0:],
				 'playerIds': playerIds[0:] }
	
	except:
		return { 'fail': 'Failed to find team\'s ranked record.' }