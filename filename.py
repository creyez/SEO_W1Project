import requests
import json
import pandas as pd
import sqlalchemy as db

url = "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/PLATINUM/IV?page=1&api_key=RGAPI-5e9e49a2-a955-4ee5-b714-e9ac920fc59a"
#url for League of Legends players that are ranked PLATNIUM IV
#https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
#update link every 24 hours because Development API Key resets

response = requests.get(url)
response = response.json()

print("SummonerName: " + response[0]["summonerName"])
print("Wins: " + str(response[0]["wins"]))
print("Losses: " + str(response[0]["losses"]))

df = pd.DataFrame.from_dict(response)
#converts dictionary into a pandas dataframe

print (df)

engine = db.create_engine('sqlite:///data_base_name.db')
df.to_sql('platPlayers', con=engine, if_exists='replace', index=False)
query_result = engine.execute("SELECT * FROM platPlayers;").fetchall()
print(pd.DataFrame(query_result))
