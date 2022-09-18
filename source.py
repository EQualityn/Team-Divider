import random
import pandas as pd

N_TEAMS = 4

# def n_team_participants(positions):
#     teams = []
#     for i in  range (0,N_TEAMS):
#         teams.append(positions.count(i+1))
#     return teams

data = pd.read_csv("spam.csv")
positions = [0 for x in range(len(data))]


for i in range (len(data)):
    current_team=i%N_TEAMS+1
    current_pos = random.randint(0,len(data)-1)
    if positions[current_pos]!=0:
      while positions[current_pos]!=0:
        current_pos = random.randint(0,len(data)-1) 
    positions[current_pos]=current_team


for i in range (len(data)):
    data.loc[i, 'number'] = positions[i]
data.to_csv("spam.csv", index=False)