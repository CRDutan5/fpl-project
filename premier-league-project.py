# https://fantasy.premierleague.com/api/bootstrap-static/

import requests
import json

main_api = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()

players = main_api['elements']

teams = main_api['teams']

goalkeepers = []
defenders = []
midfielders = []
forwards = []

for player in players:
    if player["element_type"] == 1:
        goalkeepers.append(player)
    elif player["element_type"] == 2:
        defenders.append(player)
    elif player["element_type"] == 3:
        midfielders.append(player)
    elif player["element_type"] == 4:
        forwards.append(player)

player_data = {
    "goalkeepers": goalkeepers,
    "defenders": defenders,
    "midfielders": midfielders,
    "forwards": forwards
}

# Things to note "w" will overwrite, could use this for cron job
with open("players.json", "w") as json_file:
    json.dump(player_data, json_file, indent=4)

print(len(player_data["midfielders"]))

    

# print(json.dumps(attackers, indent=4))