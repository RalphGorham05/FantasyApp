from functions import *
from Player import *


class Team:
    def __init__(self):
        self.name = ''
        self.players = []
        self.stats = []
        self.url = ''

    def get_url(self):
        for team in urls:
            if self.name == str(team):
                self.url = urls[str(team)]

    #gets list of players on team
    def get_players(self):

        code = process_Site(self.url)
        playerTable = code.find('table')
        rows = playerTable.findChildren('tr')[2:]
        for row in rows:
            data = row.findChildren('td')
            player = data[1].text
            self.players.append(player)

        


    def get_stats(self):
        team_url = 'http://espn.go.com/nba/hollinger/teamstats/_/sort/defensiveEff/order/false'
        t_stats = get_HTML_Table(team_url, 'table', 0)

        team_row = t_stats.index(self.name)
        stats = t_stats[team_row-1:team_row + 11]
        del stats[1]

    
        #Get the stats that I want
        team_rank = stats[0]
        team_pace = stats[1]
        team_assists = stats[2]
        team_rebs = stats[6]
        team_off_efficiency = stats[9]
        team_def_efficiency = stats[10]

        print('\t '.join(map(str, stats)))


t = Team()
t.get_url()
u = t.url

t.get_players()
players = t.players

for player in players:
    p = Player(str(player))
    p.get_pID(u)
    print p.name, p.pid
