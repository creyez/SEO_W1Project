import requests
import json
import sqlalchemy as db

url = "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/PLATINUM/IV?page=1&api_key=RGAPI-5e9e49a2-a955-4ee5-b714-e9ac920fc59a"
#url for League of Legends players that are ranked PLATNIUM IV
#https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
#update link every 24 hours because Development API Key resets

response = requests.get(url)
json_data = json.loads(response.text)
#converts the request to a dictionary

print("SummonerName: " + json_data[0]["summonerName"])
print("Wins: " + str(json_data[0]["wins"]))
print("Losses: " + str(json_data[0]["losses"]))

print(type(json_data))

# engine = db.create_engine('sqlite:///data_base_name.db')
