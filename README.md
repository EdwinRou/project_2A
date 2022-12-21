# project_2A
Projet d'informatique du cours "Python pour la datascience" de deuxième année de l'ENSAE.

Le but du projet est d'utiliser divers méthodes de machine learning afin de prédire le résultat d'une partie sur le jeu League of Legends, en utilisant les informations donné lors de la "champ select"(momment où chaque joueurs choisis son personnage pour la partie).

## Enjeu :

Les joueurs peuvent quitter une « champ select » sans grande conséquence (beaucoup moins pénalisant qu'une défaite) puisque la partie n’a pas encore démarré. Ainsi, le fait de pouvoir prédire le résultat avant même le début de la partie pourrait permettre d’éviter les parties a priori perdues d’avance, du fait d’une différence trop forte entre les deux équipes.
De plus le projet nous parraissait intéressant et utilisait beaucoup d'outils classique en data science (utilisation d'Api, scapping, etc).

## Description du jeu League of Legends :

Ce jeu se joue en 5 contre 5 sur une unique map, avec un Blue side et un Red side. Le jeu possède un très grand nombre de personnages différents, appelés champions.
Les 5 joueurs d'une même équipe ont chacun un rôle différent : Top, Jungle, Mid, Carry, Support.
Lors de la "champ select" chaque joueur a un rôle prédeterminé et choisis son champion. Les pseudos et champions des 5 joueurs de chaque équipes sont visibles à la fin de celle-ci, quelques secondes avant le lancement d'une partie.
Notre objectif est d'utiliser seulement ces paramètres et d'essayer de prédire le résultat de la partie.

## Problématique :

Quelles caractéristiques sur les joueurs permettent de prédire le résultat d'une partie sur League of Legends?

## Description de notre stratégie pour créer le dataset :

Tout d'abord nous avons utilisé l'Api de Riot, l'éditeur du jeu, afin de construire une base de donnée de parties compétitves à haut elo.
Ensuite nous avons utilisé des méthodes de scraping sur le site [https://www.leagueofgraphs.com/ ](https://www.leagueofgraphs.com/fr/) afin de récupérer des features intéressantes sur le profil des joueurs.
Nous avons choisis d'utiliser le win rate sur le champion choisis, ainsi que le nombre de parties jouées avec le champions choisis.

Nous avons donc contruit de cette manière un dataframe de 3500 parties compétitives. Pour chaque partie, il y a le winrate de chaques joueurs sur le champion choisis ainsi que le nombre de partie joués avec ce champion.

Nous avons ensuite rajouté les variables correspondant à la moyenne du win rate (taux de victoire) et la moyenne du nombre de parties au seins d'une équipe : blue_winrates_avg et red_winrates_avg et blue_games_avg et red_games_avg ; ainsi que avg_win_dif = blue_winrates_avg - red_winrates_avg.


## Description des modèles de machine learning :

Nous avons tout d'abord traité le jeu de données, notamment afin de remplacer les données manquantes.

Nous avons utilisé une regression logistique étant donné que la variable à prédire est binaire. Nous avons obtenu une précision de 83%.

Nous avons également fait des tests sur un modèle d'arbre de décision.
Nous avons ensuite continué avec un modèle de random forest. Après avoir calibrer les hyperparamètres, nous avons obtenu une précision de 82%.



# Notebook Final

Le Notebook final contient la majeure partie de notre projet, certains programmes ont été mis à part pour alléger le rendu, notamment la partie utilisant l'API qui se trouve dans le dossier RiotApi ainsi que les programmes permettant de modéliser les graphiques dans la partie II.
https://github.com/EdwinRou/project_2A/blob/c394133911422b427097f026cda09cf85f6d9f1b/Notebook.ipynb
