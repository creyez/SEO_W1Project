# SEO Week 1 Project: LoL Wins & Losses
Compare your League of Legends win rate with a random player.

## Description
This project asks the user to input their SummonerID for League of Legends and compares their ranked solo win rate to a random Summoner in the same division.\
\
Uses the League of Legends API:
* Used to get the wins and losses of a random summoner:
    * https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
* Used to get the wins and losses of a specific summoner:
    * https://developer.riotgames.com/apis#league-v4/GET_getLeagueEntries
* Used to get API Key (updates every 24 hours):
    * https://developer.riotgames.com/

## Dependencies
Uses the following libraries:
* requests
* pandas 
* sqlalchemy 

```bash
python -m pip install requests
pip3 install pandas
pip install SQLAlchemy
```

## Usage
```python
id = input('Enter your League of Legends SummonerID: ')

# returns encrypted account ID to use in API
accountID = getAccountID(id)

# returns account info (including rank, wins, losses) based on encrypted ID
accountInfo = getSummonerStats(accountID)

# returns the ranked Solo stats of the given player or an empty list if the player has not played ranked solo recently
rSoloStats = rankedSoloStats(accountInfo)

# returns a dictionary of random players in the same ranking as the given player
randomSummoners = getRandomPlayers(rSoloStats)

# prints messages comparing the stats of a random player's and the given player's ranked solo performance
compareToRandom(rSoloStats, randomSummoners)

# prints a dataframe of random players in the same ranking and creates a database with the same information
createDataBase(randomSummoners)
```

## Badges


![example workflow](https://github.com/creyez/SEO_W1Project/actions/workflows/style.yaml/badge.svg) \
![example workflow](https://github.com/creyez/SEO_W1Project/actions/workflows/test.yaml/badge.svg)
