import pdb
import requests
import pprint
import credentials

session = requests.Session()


url = 'https://users.premierleague.com/accounts/login/'
payload = {
 'password': credentials.password,
 'login': credentials.username,
 'redirect_uri': 'https://fantasy.premierleague.com/a/login',
 'app': 'plfpl-web'
}
session.post(url, data=payload)

responseJson = session.get('https://fantasy.premierleague.com/api/my-team/' + str(credentials.team_id)).json()
# {chips: {}, picks:{}, transfers:{}}
pprint.pprint(responseJson) 