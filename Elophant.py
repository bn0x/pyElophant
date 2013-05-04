"""
Import our modules
"""

import urllib2
import urllib
import json

"""
Make sure to put in your API Key
"""
apiKey = 'Put your API Key here'

"""
The function to get summoner stats and return them.
'fail' is the only way to detect if an exception occured until I find another way.
"""

def SummonerStats(region, requestData):
	try:
		if ' ' in requestData:
			requestData = requestData.replace(' ', '%20')
		apiURL = 'http://api.elophant.com/v2/' + region + '/' + 'summoner' + '/' + requestData + '?key=' + apiKey
		summonerURLOpen = urllib2.urlopen(apiURL)
		summonerJSON = json.load(summonerURLOpen)
		return { 'summonerLevel': summonerJSON['data']['summonerLevel'], 'name': summonerJSON['data']['name'], 'internalName': summonerJSON['data']['internalName'], 'revisionDate': summonerJSON['data']['revisionDate'], 'profileIconId': summonerJSON['data']['profileIconId'], 'acctId': summonerJSON['data']['acctId'], 'summonerId': summonerJSON['data']['summonerId'] }
	except:
		return { 'fail': 'Failed to get summoner stats.' }