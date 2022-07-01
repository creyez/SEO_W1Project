import os
import requests
import pandas as pd
import sqlalchemy as db


def testFuction(inp1):
    return inp1


APIKey = "RGAPI-15448d20-caa7-4173-8bbc-d6f432e8adf9"
id = input('Enter your League of Legends SummonerID: ')


def getAccountID(idInput):
      url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str(idInput).replace(" ", "%20") + "?api_key=" + APIKey
      response = requests.get(url)
      response = response.json()

      if "status" in response:
          newID = input('Summoner not found. Enter SummonerID: ')
          getAccountID(newID)
      else:
          return response['id']


def getSummonerStats(accountIDInput):
    url = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(accountIDInput) + "?api_key=" + APIKey
    response = requests.get(url)
    response = response.json()
    return response

def playsRanked(yourStats):
    rankedSolo = False;

    if len(yourStats) == 0:
        print("This player does not play ranked")

    for queues in yourStats:
        if 'queueType' in queues:
            if queues['queueType'] == 'RANKED_SOLO_5x5':
                rankedSolo = True
                stats = queues

    if rankedSolo == True:
        print("plays RankedSOLO")
    else:
        print("does not play solo")



accountID = getAccountID(id)
os.system("xEzTheKingx")
accountInfo = getSummonerStats(accountID)
print(accountInfo[0]['wins'])
# playsRanked(accountInfo)



# print(accountInfo[0]['wins'])

'''
create a function for user input, 
      ask for rank and division

create a method that will create the url 
      based on the rank, division, and 
      api key and return the response
      
create a method that turns the .json to a data base
'''


url = "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/PLATINUM/IV?page=1&api_key=RGAPI-15448d20-caa7-4173-8bbc-d6f432e8adf9"

# url for League of Legends players that are ranked PLATNIUM IV
# https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
# update link every 24 hours because Development API Key resets

# response = requests.get(url)
# response = response.json()
#
# print("SummonerName: " + response[0]["summonerName"])
# print("Wins: " + str(response[0]["wins"]))
# print("Losses: " + str(response[0]["losses"]))
#
# df = pd.DataFrame.from_dict(response)
# # converts dictionary into a pandas dataframe
# print(df)
#
# engine = db.create_engine('sqlite:///data_base_name.db')
# df.to_sql('platPlayers', con=engine, if_exists='replace', index=False)
# query_result = engine.execute("SELECT * FROM platPlayers;").fetchall()
# print(pd.DataFrame(query_result))
# # converts pandas dataframe to a data base
