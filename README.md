# Team builder model predictor

In this project I built an engine that could help Liga NOS's coaches build their team before a game.
Data Collection: 
- Gather data of 3 and a half seasons;
- Web scrapping zerozero.pt (Gathering which players played in each game);
- Acquire datasets on football-data.co.uk (Gathering the stats of each game).

Data Wrangling:
- Transform datasets into a suitable dataframe in order to train and test the machine learning model;
- The main dataset is the difference between the home team's stats and the away team's stats.

Caracterization of Liga NOS's teams and players: https://public.tableau.com/profile/tom.s.marques#!/vizhome/LigaNOS_16154766812000/Dashboard1

Machine Learning model (Decision tree): 
- Predicts the result of a game
Uses these stats to predict the result:
- Half time goals;
- Corners;
- Fouls committed;
- Shots;
- Shots on target;
- Yellow cards;
- Red cards.

Product: result_predictor_liga_nos.py

Script to gather the data: Scrap Football stats 2.ipynb

Script to build the model: model_final_project.ipynb
