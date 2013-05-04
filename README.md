pyElophant
==========

Python libary for Elophant API (easy to use)
Make sure to put your API key in Elophant.py



Libary/Module use example
=========================
Make sure to put your API key in Elophant.py
<pre>
"""
Import our module 
"""

import Elophant

"""
Getting inputs to store in variables
"""

summonerName = raw_input("Summoner Name: ")
region = raw_input("Region: ")

"""
Call the function to get data.
"""

stats = Elophant.SummonerStats(region, summonerName)

"""
Check if it failed. (Python exception)
"""
try:
	if stats['fail']:
		print stats['fail']
except:
	pass
"""
Print the output from the API
"""
print stats['summonerLevel']
print stats['name']
print stats['internalName']
print stats['revisionDate']
print stats['profileIconId']
print stats['acctId']
print stats['summonerId']
</pre>
