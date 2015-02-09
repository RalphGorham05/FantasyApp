from bs4 import BeautifulSoup
#from peeewee import *
from multiprocessing import Pool
import multiprocessing
import threading
from datetime import datetime, time
import re
from mechanize import Browser

pl = raw_input('Enter player name: ')


#pool = Pool(8)


##################Team URLs section###################

#Atlantic Division
celtics = 'http://espn.go.com/nba/team/roster/_/name/bos/boston-celtics'
nets = 'http://espn.go.com/nba/team/roster/_/name/bkn/brooklyn-nets'
knicks = 'http://espn.go.com/nba/team/roster/_/name/ny/new-york-knicks'
sixers = 'http://espn.go.com/nba/team/roster/_/name/phi/philadelphia-76ers'
raptors = 'http://espn.go.com/nba/team/roster/_/name/tor/toronto-raptors'

atlantic = [celtics, nets, knicks, sixers, raptors]

#Central Division
bulls = 'http://espn.go.com/nba/team/roster/_/name/chi/chicago-bulls'
cavs = 'http://espn.go.com/nba/team/roster/_/name/cle/cleveland-cavaliers'
pistons = 'http://espn.go.com/nba/team/roster/_/name/det/detroit-pistons'
pacers = 'http://espn.go.com/nba/team/roster/_/name/ind/indiana-pacers'
bucks = 'http://espn.go.com/nba/team/roster/_/name/mil/milwaukee-bucks'

central = [bulls, cavs, pistons, pacers, bucks]

#SE Division
hawks = 'http://espn.go.com/nba/team/roster/_/name/atl/atlanta-hawks'
hornets = 'http://espn.go.com/nba/team/roster/_/name/cha/charlotte-hornets'
heat = 'http://espn.go.com/nba/team/roster/_/name/mia/miami-heat'
magic = 'http://espn.go.com/nba/team/roster/_/name/orl/orlando-magic'
wizards = 'http://espn.go.com/nba/team/roster/_/name/wsh/washington-wizards'

se = [hawks, hornets, heat, magic, wizards]


#northwest division
nuggets = 'http://espn.go.com/nba/team/roster/_/name/den/denver-nuggets'
twolves = 'http://espn.go.com/nba/team/roster/_/name/min/minnesota-timberwolves'
thunder = 'http://espn.go.com/nba/team/roster/_/name/okc/oklahoma-city-thunder'
blazers = 'http://espn.go.com/nba/team/roster/_/name/por/portland-trail-blazers'
jazz = 'http://espn.go.com/nba/team/roster/_/name/utah/utah-jazz'

nw = [nuggets, twolves, thunder, blazers, jazz]

#southwest division
mavs = 'http://espn.go.com/nba/team/roster/_/name/dal/dallas-mavericks'
rockets = 'http://espn.go.com/nba/team/roster/_/name/hou/houston-rockets'
grizzlies = 'http://espn.go.com/nba/team/roster/_/name/mem/memphis-grizzlies'
pelicans = 'http://espn.go.com/nba/team/roster/_/name/no/new-orleans-pelicans'
spurs = 'http://espn.go.com/nba/team/roster/_/name/sa/san-antonio-spurs'

sw = [mavs, rockets, grizzlies, pelicans, spurs]

#pacific division
warriors = 'http://espn.go.com/nba/team/roster/_/name/gs/golden-state-warriors'
clippers = 'http://espn.go.com/nba/team/roster/_/name/lac/los-angeles-clippers'
lakers = 'http://espn.go.com/nba/team/roster/_/name/lal/los-angeles-lakers'
suns = 'http://espn.go.com/nba/team/roster/_/name/phx/phoenix-suns'
kings = 'http://espn.go.com/nba/team/roster/_/name/sac/sacramento-kings'

pacific = [warriors, clippers, lakers, suns, kings]


nba = [atlantic, central, se, nw, sw, pacific]




###############functions section##################


def get_teamStats(team_name):
    team_url = 'http://espn.go.com/nba/hollinger/teamstats/_/sort/defensiveEff/order/false'
    t_stats = get_HTML_Table(team_url, 'table', 0)

    team_row = t_stats.index(team_name)
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


    
    

#preps site for access and returns BSoup object        
def process_Site(url):
    browser = Browser()
    u = browser.open(url)
    page = u.read()
    source = BeautifulSoup(page)

    return source

#parses table by row and returns a list with each row as element
def parse_Table(table):
    data = []
    rows = table.findChildren('tr')[2:]
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.text
            info = value.lower()
            data.append(info)

    return data


#parses site and return table with data
def get_HTML_Table(url, data, table_number = 0):
    processed = process_Site(url)
    data_table = processed.findAll(data)[table_number]
    table = parse_Table(data_table)

    return table


#splits the Team string to get only the city name
def team_Name(e):
    teamString = e.split('/')
    lastWord = len(teamString) - 1
    nameSeparated = teamString[lastWord].split('-')

    #accounts for teams with cities with 2 word names(i.e LA Lakers, LA Clippers, Portland Trail Blazers)
    if len(nameSeparated) == 3:
        city = nameSeparated[0] + ' ' + nameSeparated[1]
        if city == 'portland trail':
            city = 'portland'
        elif city == 'los angeles':
            city = 'la' + ' ' + nameSeparated[2]
        
    else:
        city = nameSeparated[0]

    return city



#check to find team
team_list = []
def get_Team(player, divs):
    tName = ''
    for division in divs:
        for team in division:
            code = process_Site(team)
            playerTable = code.find('table')

            #make list of all the teams
            team_list.append(team_Name(team))
            
            

            rows = playerTable.findChildren('tr')[2:]
            for row in rows:
                data = row.findChildren('td')
                name = data[1].text
                if player == name:
                    tName = team_Name(team)
                
                    
    return tName




###########Program start#######################################################



#start = time.clock()
city_name = get_Team(pl, nba)
print pl + ' plays for ' + city_name
#end = time.clock()
#print end - start



##############Schedule section##############


#Get the daily schedule



schedule_url = 'http://espn.go.com/nba/schedule'
sched = process_Site(schedule_url)

now = datetime.now()
current_time = now.time()
#today = time.strftime('%A' + ', ' + '%B' + ' ' + "%s" %now.day)

if time(12,00) <= current_time <= time(23,59):
    schedule = get_HTML_Table(schedule_url, 'table', 0)
    
else:
    schedule = get_HTML_Table(schedule_url, 'table', 1)
    


#Create list of games scheduled for current date
today_games = []

today_games.append(schedule[0])
for game in range(6, len(schedule), 6):
    today_games.append(schedule[game])



#checks if player is playing today
for each_game in today_games:
    games = each_game.split()
    names_size = len(games)

    if names_size == 5:
        games[0] = games[0] + ' ' + games[1]
        games[1] = games[3] + ' ' + games[4]
        del games[2:]

    elif names_size == 4 and games[1] == 'at':
        games[1] = games[2] + ' ' + games[3]
        del games[2:]
        
    elif names_size == 4:
        games[0] = games[0] + ' ' + games[1]
        games[1] = games[names_size - 1]
        del games[2:]

    elif names_size == 3:
        games[1] = games[2]
        del games[2:]

############Team Stats section#################
'''
    if city_name in games:
        for g in games:
            print g
            print 'Defensive Rank \t Pace \t Ast \t Rebs \t Off Efficiency \t Def Efficiency'
            print ' '
            print get_teamStats(g)

'''


position_url = 'http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings'

position_def = get_HTML_Table(position_url, 'table', 0)

t_name = city_name.split()
#print t_name[1]

'''
position_stats = []
r = 0
for r in range(r,len(position_def),14):
    position_stats.append(position_def[r:r + 14])

for p in position_stats:
    if city_name in p:
        print p

'''


nba_url = 'http://stats.nba.com/tracking/#!/player/possessions/'

possessions = get_HTML_Table(nba_url, 'table')

for p in possessions:
    print p



