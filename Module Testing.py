import Elophant

summonerName = raw_input("Summoner Name: ")
#summonerName = str(summonerName)
region = raw_input("Region: ")
#region = str(region)
stats = Elophant.SummonerStats(region, summonerName)
try:
	if stats['fail']:
		print stats['fail']
except:
	pass

print stats['summonerLevel']
print stats['name']
print stats['internalName']
print stats['revisionDate']
print stats['profileIconId']
print stats['acctId']
print stats['summonerId']