import requests
import time
import pandas as pd
import numpy as np

division = "DIAMOND"

def summ_ID_puller(api_key):
    for tier in ["I", "II", "III", "IV"]:
        for page in range(1, 20):
            time.sleep(0.1)
            url_pull = "https://euw1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/{}/{}?page={}&api_key={}".format(
                    division, tier, page, api_key)
            profile_list = requests.get(url_pull).json()
            summID_list = []

            for profile in range(len(profile_list)):
                summID_list.append(profile_list[profile]['summonerId'])

            df = pd.DataFrame(summID_list, columns=["Summoner ID"])
            df.to_csv('summID.csv', mode='a')
