"""
Import our module 
"""

import Elophant
import sys

"""
Getting inputs to store in variables
"""

summonerName = raw_input("Summoner Name: ")
region = raw_input("Region: ")

"""
Call the function to get data.
"""


tier = Elophant.summonerLeagues(region, summonerName)
try:
	print(' ')
	print summonerName, 'ranked stats: '
	print tier['tier'], tier['league'], tier['rank']
	print tier['previousDayLeaguePosition']
	print tier['hotStreak']
	print tier['freshBlood']
	print tier['lastPlayed']
	print tier['playerOrTeamId']
	print tier['inactive']
	print tier['veteran']
	print tier['queueType']
	print tier['losses']
	print tier['playerOrTeamName']
	print tier['wins']
except:
	print tier['fail']
	pass
"""
Check if it failed. (Python exception)
"""

"""
Print the output from the API
"""
stats = Elophant.summonerStats(region, summonerName)

try:
	print '\n'
	print 'Summoner stats of:', summonerName
	print stats['summonerLevel']
	print stats['name']
	print stats['internalName']
	print stats['revisionDate']
	print stats['profileIconId']
	print stats['acctId']
	print stats['summonerId']
except:
	print stats['fail']
	sys.exit('gg')