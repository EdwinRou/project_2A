import requests
import time
import pandas as pd
import numpy as np

summoner_IDs = pd.read_csv("summID.csv")
accountID_list = []
summID_list = summoner_IDs["Summoner ID"]

def acct_ID_puller(api_key):

    for summID_idx in range(0, 100):
        time.sleep(0.1)
        if summID_list[summID_idx] == "Summoner ID":
            pass
        else:
            url_acct_pull = "https://{}.api.riotgames.com/lol/summoner/v4/summoners/{}?api_key={}".format(
                region, summID, api_key)
            account_info = requests.get(url_acct_pull).json()
            accountID_list.append(account_info["puuid"])
    return accountID_list
