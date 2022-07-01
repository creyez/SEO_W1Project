# SEO Week 1 Project: LoL Wins & Losses
Compare your League of Legends win rate with a random player.

## Description
This project asks the user to input their SummonerID for League of Legends and will compare their ranked win rate to a random Summoner in their same rank division.\
\
Uses the League of Legends API:
* Used to get the wins and losses of a random summoner:
    * https://developer.riotgames.com/apis#league-exp-v4/GET_getLeagueEntries
* Used to get the wins and losses of a specific summoner
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
Show commands here...

#
## Badges


![example workflow](https://github.com/creyez/SEO_W1Project/actions/workflows/style.yaml/badge.svg) \
![example workflow](https://github.com/creyez/SEO_W1Project/actions/workflows/test.yaml/badge.svg)
