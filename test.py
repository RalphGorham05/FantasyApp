from mechanize import Browser
from bs4 import BeautifulSoup
from functions import process_Site


pid = 2745
url = 'http://espn.go.com/nba/team/roster/_/name/sac/sacramento-kings'

def get_players(team):
    players = []

    code = process_Site(team)
    playerTable = code.find('table')
    rows = playerTable.findChildren('tr')[2:]
    for row in rows:
        data = row.findChildren('td')
        name = data[1].text
        players.append(name)

    return players
    
    



l = get_players(url)
for k in l:
    print k

   
    
        
    

