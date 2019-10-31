# encoding: utf-8
import pdb
import requests
import pprint
import json
import sys

# Loading general info locally into JSON file player_data.json
def load_general_info():
    general_url = "https://fantasy.premierleague.com/api/bootstrap-static/"
    general_data = requests.get(url=general_url).json()
    elements = general_data['elements']
    player_info = {}
    for element in elements:
        player_info[element['id']] = element
    f = open("player_data.json","w")
    f.write(json)
    f.close()

# Loading team data locally into JSON file team_data.json
def load_my_team(username, password, team_id):
    session = requests.Session()
    # Login
    login_url = 'https://users.premierleague.com/accounts/login/'
    payload = {
    'password': password,
    'login': username,
    'redirect_uri': 'https://fantasy.premierleague.com/a/login',
    'app': 'plfpl-web'
    }
    session.post(login_url, data=payload)
    teamInfo = session.get('https://fantasy.premierleague.com/api/my-team/' + str(team_id)).json()
    data = json.dumps(teamInfo)
    f = open("team_data.json","w")
    f.write(data)
    f.close()


with open('player_data.json') as json_file:
    player_data = json.load(json_file)

with open('credentials.json') as json_file:
    credentials = json.load(json_file)

with open('team_data.json') as json_file:
    team_data = json.load(json_file)

# load_my_team(credentials["username"], credentials["password"], credentials["team_id"])

for pick in team_data['picks']:
    pprint.pprint(player_data[str(pick['element'])]["web_name"].encode('unicode_escape'))
# pprint.pprint(responseJson) 

"""
API ENDPOINTS:
1. https://fantasy.premierleague.com/api/entry/{team-id}}/ : info about your team like leagues, name etc
2. https://fantasy.premierleague.com/api/element-summary/{player-id}/ : in depth info of players history, fixtures
3. https://fantasy.premierleague.com/api/my-team/{team-id}' : Picks, chips, transfers
4. https://fantasy.premierleague.com/api/bootstrap-static/ : General FPL info

"""