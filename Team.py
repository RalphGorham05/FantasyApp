from functions import *
from Player import *


class Team:
    def __init__(self):
        self.name = ''
        self.players = []
        self.stats = []
        self.url = ''
        self.positionStats = []


    #gets the team's url
    def get_url(self):
        for page in urls:
            if self.name == str(page):
                self.url = urls[str(page)]


    #gets list of players on team
    def get_players(self):
        code = process_Site(self.url)
        playerTable = code.find('table')
        rows = playerTable.findChildren('tr')[2:]

        for row in rows:
            data = row.findChildren('td')
            player = data[1].text
            self.players.append(player)


    #gets team stats
    def get_stats(self):
        team_url = 'http://espn.go.com/nba/hollinger/teamstats/_/sort/defensiveEff/order/false'
        stats_table = get_HTML_Table(team_url, 'table', 0)
        team_row = stats_table.index(self.name)
        team_stats = stats_table[team_row-1:team_row + 11]
        del team_stats[1]

        self.stats.append('\t '.join(map(str, team_stats)))

    def get_stats_vs_position(self):
        position_url = 'http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings'
        pos_stats = []
        team_start = 0


        position_def = get_HTML_Table(position_url, 'table', 0)

        for team_start in range(team_start,len(position_def), 14):
            pos_stats.append(position_def[team_start:team_start + 14])


        for row in pos_stats:
            teams_col = team_Name(row[0])


            if self.name in teams_col:
                self.positionStats = row




t = Team()
t.name = 'mavericks'
t.get_stats_vs_position()
print t.positionStats[2]
t.get_url()
u = t.url
t.get_players()

players = t.players

for player in players:
    p = Player(str(player))
    p.get_pID(u)
    print p.name, p.pid

