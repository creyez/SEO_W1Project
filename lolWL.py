import requests
import random
import pandas as pd
import sqlalchemy as db


def testFuction(inp1):
    return inp1


APIKey = ""
id = input('Enter your League of Legends SummonerID: ')


def getAccountID(idInput):
    url = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + str(idInput).replace(" ",
                                                                                                    "%20") + "?api_key=" + APIKey
    response = requests.get(url)
    response = response.json()

    if "status" in response:
        newID = input('Summoner not found. Enter SummonerID: ')
        getAccountID(newID)
    else:
        return response['id']


def getSummonerStats(accountIDInput):
    url = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + str(
        accountIDInput) + "?api_key=" + APIKey
    response = requests.get(url)
    response = response.json()
    return response


def rankedSoloStats(yourStats):
    rankedSolo = False;

    if len(yourStats) == 0:
        return []

    for queues in yourStats:
        if 'queueType' in queues:
            if queues['queueType'] == 'RANKED_SOLO_5x5':
                rankedSolo = True
                stats = queues

    if rankedSolo == True:
        return stats
    else:
        return []


def getRandomPlayers(rSoloStats):
    if len(rSoloStats) == 0:
        print("This summoner has not played enough ranked solo recently")
        return -1
    else:
        url = "https://na1.api.riotgames.com/lol/league-exp/v4/entries/RANKED_SOLO_5x5/" + rSoloStats['tier'] + "/" + \
              rSoloStats['rank'] + "?page=1&api_key=" + APIKey
        response = requests.get(url)
        response = response.json()
        return response


def compareToRandom(yourStats, randomPlayers):
    if len(yourStats) == 0:
        return -1

    randPlayer = randomPlayers[random.randint(0, len(randomPlayers) - 1)]

    print()
    print("Here are your stats:")
    print("    SummonerName: " + yourStats["summonerName"])
    print("    Wins: " + str(yourStats["wins"]))
    print("    Losses: " + str(yourStats["losses"]))
    print()
    print("These are the stats of a random Summoner in the same division:")
    print("    SummonerName: " + randPlayer["summonerName"])
    print("    Wins: " + str(randPlayer["wins"]))
    print("    Losses: " + str(randPlayer["losses"]))
    print()

    yWR = round(((yourStats["wins"] / (yourStats["losses"] + yourStats["wins"])) * 100), 2)
    rWR = round(((randPlayer["wins"] / (randPlayer["losses"] + randPlayer["wins"])) * 100), 2)

    print(
        "You have a " + str(yWR) + "% win rate, compared to " + randPlayer[
            "summonerName"] + "\'s " + str(rWR) + "% win rate")

def createDataBase(randomPlayers):
    if randomPlayers == -1:
        return -1
    df = pd.DataFrame.from_dict(randomPlayers)
    # converts dictionary into a pandas dataframe

    print()
    print()
    print("Here is a table of other random players in the same division:")
    print()
    print(df)
    engine = db.create_engine('sqlite:///data_base_name.db')
    df.to_sql('platPlayers', con=engine, if_exists='replace', index=False)
    query_result = engine.execute("SELECT * FROM platPlayers;").fetchall()
    # converts pandas dataframe to a data base


accountID = getAccountID(id)
accountInfo = getSummonerStats(accountID)
rSoloStats = rankedSoloStats(accountInfo)
randomSummoners = getRandomPlayers(rSoloStats)
compareToRandom(rSoloStats, randomSummoners)
createDataBase(randomSummoners)



