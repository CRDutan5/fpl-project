# https://fantasy.premierleague.com/api/bootstrap-static/

import requests
import json

response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/").json()

players = response['elements']

top_players = sorted(players, key=lambda player:player["total_points"], reverse=True)[:10]


print(json.dumps(top_players, indent=4))
