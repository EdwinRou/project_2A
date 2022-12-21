# project_2A
Projet d'info de deuxième année de l'ENSAE

Le but du projet est d'utiliser divers methodes de machine learning afin de prédire le résultat d'une partie sur le jeu League of Legends, en utilisant les informations donné lors de la "champ select"(momment ou chaque joueurs choisis son personnage pour la partie).

## Description du jeu League of Legends :

Ce jeu se joue en 5 contre 5 sur une unique map, avec un Blue side et un Red dide. Le jeu possède un très grand nombre de personnages différents, appelés champions.
Les 5 joueurs d'une même équipe ont chacun un rôle différent : Top, Jngl, Mid, Carry, Support.
Lors de la "champ select" chaque joueur a un rôle prédeterminé et choisis son champion. Les pseudos et champions des 5 joueurs de chaque équipes sont visibles à la fin de celle-ci, quelques secondes avant le lancement d'une partie.
Notre objectif est d'utiliser seulement ces paramètres et d'essayer de prédire le résultat de la partie.

## Description of our strategy to create our data :

Tout d'abord nous avons utilisé l'Api de Riot, l'éditeur du jeu, afin de construire une base de donnée de parties compétitves à haut elo.
Ensuite nous avons utilisé des méthodes de scraping sur le site [https://www.leagueofgraphs.com/ ](https://www.leagueofgraphs.com/fr/) afin de récupérer des features intéressantes sur le profil des joueurs.

Nous avons donc contruit un dataframe de 3500 parties compétitives. Pour chaque partie, il y a le winrate de chaques joueurs sur le champion choisis ainsi que le nombre de partie joués avec ce champion.


## Description of our ML models :


# Notebook Final
https://github.com/EdwinRou/project_2A/blob/c394133911422b427097f026cda09cf85f6d9f1b/Notebook.ipynb
