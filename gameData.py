import requests
import time
import pandas as pd
import numpy as np


#Variables :

matchIDs = pd.read_csv("MatchId.csv")
positions = ["Blue Top", "Blue Jungle", "Blue Mid", "Blue Carry", "Blue Support", "Red Top", "Red Jungle", "Red Mid", "Red Carry", "Red Support", "Outcome"]


#Programmes :

def match_data_collector (gameID):
    match_url = "https://europe.api.riotgames.com/lol/match/v5/matches/{}?api_key={}".format(gameID ,api_key)
    match_api_data = requests.get(match_url).json()
    match_data = np.empty(10, dtype = object)
    for i in range(len(match_api_data['info']['participants'])):
        participant_info = match_api_data['info']['participants'][i]
        summonerName = participant_info["summonerName"]
        teamPosition = participant_info["teamPosition"]
        teamId = participant_info["teamId"]
        championName = participant_info["championName"]
        if participant_info["win"] == True :
            outcome = 'Victoire'
        else :
            outcome = 'Défaite'
        if teamId == 100 :
            if teamPosition == 'TOP':
                match_data[0] = [summonerName,championName,'Blue Top', outcome]
            elif teamPosition == 'JUNGLE':
                match_data[1] = [summonerName,championName,'Blue Jungle', outcome]
            elif teamPosition == 'MIDDLE':
                match_data[2] = [summonerName,championName,'Blue Mid', outcome]
            elif teamPosition == 'BOTTOM':
                match_data[3] = [summonerName,championName,'Blue Carry', outcome]
            elif teamPosition == 'UTILITY':
                match_data[4] = [summonerName,championName,'Blue Support', outcome]
            else :
                print( teamPosition , summonerName , championName , teamId , "not found" )
        elif teamId == 200 :
            if teamPosition == 'TOP':
                match_data[5] = [summonerName,championName,'Red Top', outcome]
            elif teamPosition == 'JUNGLE':
                match_data[6] = [summonerName,championName,'Red Jungle', outcome]
            elif teamPosition == 'MIDDLE':
                match_data[7] = [summonerName,championName,'Red Mid', outcome]
            elif teamPosition == 'BOTTOM':
                match_data[8] = [summonerName,championName,'Red Carry', outcome]
            elif teamPosition == 'UTILITY':
                match_data[9] = [summonerName,championName,'Red Support', outcome]
            else :
                print( teamPosition , summonerName , championName , teamId , "not found" )
        else :
            print ( teamPosition , summonerName , championName , teamId ,"team not found" )
    return match_data


#Récupération des données pour octobre
def match_data_oct (nb_parties) :
    games_data_oct = np.empty([matchIDs.shape[0],11], dtype = object)
    for i in range(0, nb_parties) :
            #range(0, len(matchIDs["Octobre"])) si on veut obtenir l'historique de toutes les games, mais le programme va tourner pendant plus de 3h
        try :
            time.sleep(1.5)
            infos = (match_data_collector(matchIDs["Octobre"][i]))
            if any(elem is None for elem in infos) == False :
                for j in range (len(infos)):
                    games_data_oct[i][j] = [infos[j][0], infos[j][1]]
                if infos[0][3] == 'Victoire':
                    games_data_oct[i][10] = 'Victoire des Bleus'
                else :
                    games_data_oct[i][10] = 'Victoire des Rouges'
        except KeyError :
            print("keyerror")
            break
    df_final_oct = pd.DataFrame(games_data_oct,  columns = positions)
    index_with_nan_oct = df_final_oct.index[df_final_oct.isnull().any(axis = 1)]
    df_final_oct = df_final_oct.drop(index_with_nan_oct)
    return df_final_oct



#Récupération des données pour novembre
def match_data_nov (nb_parties) :
    games_data_nov = np.empty([matchIDs.shape[0],11], dtype = object)
    for i in range(0, nb_parties) :
            #range(0, len(matchIDs["Novembre"])) si on veut obtenir l'historique de toutes les games, mais le programme va tourner pendant plus de 3h
        try :
            time.sleep(1.5)
            infos = (match_data_collector(matchIDs["Novembre"][i]))
            if any(elem is None for elem in infos) == False :
                for j in range (len(infos)):
                    games_data_nov[i][j] = [infos[j][0], infos[j][1]]
                if infos[0][3] == 'Victoire':
                    games_data_nov[i][10] = 'Victoire des Bleus'
                else :
                    games_data_nov[i][10] = 'Victoire des Rouges'
        except KeyError :
            print("keyerror")
            break
    df_final_nov = pd.DataFrame(games_data_nov,  columns = positions)
    index_with_nan_nov = df_final_nov.index[df_final_nov.isnull().any(axis = 1)]
    df_final_nov = df_final_nov.drop(index_with_nan_nov)
    return df_final_nov


    

#Mise en page du dataFrame pour une meilleure lecture

def convert_df (df_base):
    
    multi_indices = []
    for i in range(df_base.shape[0]) :
        multi_indices.append(("Partie " + str(i+1) , 'Pseudo '))
        multi_indices.append(("Partie " + str(i+1) , 'Champion'))
    multi_indices = pd.MultiIndex.from_tuples(multi_indices, names = ("Partie", "Infos"))

    games_data = np.empty([2*df_base.shape[0],11], dtype = object)
    for i in range(len(df_base)) :
        ligne = df_base.iloc[i]
        for j in range (len(ligne)-1):
            games_data[2*i][j] = ligne[j][0]
            games_data[2*i+1][j] = ligne[j][1]
        games_data[2*i][10] = ligne[10]
        games_data[2*i+1][10] = ligne[10]
    
    return pd.DataFrame(games_data, index = multi_indices, columns = positions)