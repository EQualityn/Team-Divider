import random
import pandas as pd

#number of teams to split the participants

N_TEAMS = 4

while True:
    try:
        N_TEAMS = int(input("Enter amount of teams: "))
    except ValueError:
        print("Invalid input, enter a number")
        continue
    if N_TEAMS <= 0:
        print("Invalid input, enter a number above zero")
        continue
    else:
        break


def n_team_participants(positions):
    n_in_teams = []
    for i in  range (0,N_TEAMS):
        n_in_teams.append(positions.count(i+1))
    return n_in_teams

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
    data.loc[i, 'number'] = str(positions[i])
data.to_csv("spam.csv", index=False)