import requests
import time
import pandas as pd
import numpy as np

account_IDs = pd.read_csv("accountPUUID.csv")
account_IDs_list = account_IDs["AccountPUUID"]

#La liste des dates : date exacte des débuts et fins de mois en format "Timestamp"
dates = np.array([["Octobre", [1664582400,1667260799]],["Novembre", [1667174400,1669852799]]], dtype=object)

#On définit en amont le DataFrame de travail et le DataFrame final
df_vide = pd.DataFrame(columns=[i[0] for i in dates])
df1 = df_vide.copy()

def match_ID_puller(api_key):

    for mois in dates:

        matchID_list = []
        df_travail = df_vide.copy()

        for puuid in account_IDs_list:
            time.sleep(1.5)
            url_match_pull = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{}/ids?startTime={}&endTime={}&queue=420&type=ranked&start=0&count=100&api_key={}".format(puuid, startTime=mois[1][0], endTime=mois[1][1], api_key)
            match_history = requests.get(url_match_pull).json()
            matchID_list += match_history

        df_travail[mois[0]] = matchID_list
        df1 = df1.combine_first(df_travail)
    return df1