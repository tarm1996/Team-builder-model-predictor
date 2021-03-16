import pandas as pd
import numpy as np
import pickle

players_stats_df = pd.read_excel(r"C:\Ironhack\final_project\players_stats_df.xlsx")
players_stats_df.set_index('Unnamed: 0', inplace=True)
players_of_each_team = pd.read_excel(r"C:\Ironhack\final_project\players_of_each_team.xlsx")
players_of_each_team.set_index('Team', inplace=True)
stats_by_team = pd.read_excel(r"C:\Ironhack\final_project\stats_by_team.xlsx")
stats_by_team.set_index('Team', inplace=True)

model = pickle.load(open(r"C:\Ironhack\final_project\model.p",'rb'))


def choose_team():
    buildteam_stats={}
    teams=' / '.join(players_of_each_team.index.tolist())
    x=True
    z=True


    while z:
        
        select = input(f'Choose the team you are going to play against: {teams}: ')
        if select in teams:
            opposing_team = stats_by_team.loc[select].values
            z= False
            
        else:
            print("This team doesn't exist, please choose another one.")
            continue

    print('')

    while x:
        
        select = input(f'Choose your team: {teams}: ')
        if select in teams:
            team = players_of_each_team.loc[select,'List of players']
            #team = '/'.join(team)
            x = False
            
        else:
            print("That team doesn't exist, choose again.")
            continue
    print('')
    print('These are the players from your team: ',team)

    print('')

    for i in list(range(0,11)):
        print('')
        print('Choose player number',i,': ')
        y=True
        while y:
            select = input(f'Choose a player: ')
            if select in team:
                player = players_stats_df.loc[select]
                y = False
                
                buildteam_stats[select]=player.values
            else:
                print("This player doesn't exist, please choose again.")
                print('')
                continue
        
            
    print('')  

    team_power = np.array([l.tolist() for l in buildteam_stats.values()]).mean(0)

    if model.predict([team_power - opposing_team]) == np.array(0):
        print('With this squad your team will DRAW the game!')
    elif model.predict([team_power - opposing_team]) == np.array(1):
        print('With this squad your team will LOSE the game!')
    elif model.predict([team_power - opposing_team]) == np.array(2):
        print('With this squad your team will WIN the game!')

    print('') 
    print('These are the stats of each player of your squad: ')   
    print('') 
    print(players_stats_df.loc[buildteam_stats.keys()])

choose_team()