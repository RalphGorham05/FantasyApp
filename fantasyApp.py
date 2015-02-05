from bs4 import BeautifulSoup
#from peeewee import *
from multiprocessing import Pool
import multiprocessing
import threading
import time
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


def get_Stats():
    which_stats = raw_input('Enter ra for defensive efficiency rank, p for pace, a for assists, reb for rebounds, off for offensive efficiency, and def for defensive efficiency: ')

    if which_stats == 'ra':
        print team_rank
    
    elif which_stats == 'p':
        print team_pace
    
    elif which_stats == 'a':
        print team_assists
    
    elif which_stats == 'reb':
        print team_rebs
    
    elif which_stats == 'off':
        print team_off_efficiency
    
    elif which_stats == 'def':
        print team_def_efficiency
    
    else:
        print 'wrong input'


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
def get_HTML_Table(url, data):
    processed = process_Site(url)
    data_table = processed.find(data)
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
            city = nameSeparated[0] + ' ' + nameSeparated[1] + ' ' + nameSeparated[2]
        
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




###########Program start###############

start = time.clock()
city_name = get_Team(pl, nba)
#print pl + ' plays for ' + city_name
end = time.clock()
#print end - start


############Team Stats section#################


team_url = 'http://espn.go.com/nba/hollinger/teamstats/_/sort/defensiveEff/order/false'
t_stats = get_HTML_Table(team_url,'table')


team_row = t_stats.index(city_name)
team_stats = t_stats[team_row-1:team_row + 11]

    

'''
#Get the stats that I want
team_rank = team_stats[0]
team_pace = team_stats[2]
team_assists = team_stats[3]
team_rebs = team_stats[7]
team_off_efficiency = team_stats[10]
team_def_efficiency = team_stats[11]
    

#if city_name in st:
    #get_Stats()
    #print city_name + ' gets ' + team_assists + ' assists per game'
    #print city_name + ' gets ' + team_rebs + ' rebounds per game'
    #print team_stats


'''


##############Schedule section##############


#Get the daily schedule
    
schedule_url = 'http://espn.go.com/nba/schedule'
schedule = get_HTML_Table(schedule_url, 'table')
print schedule

#Create list of games scheduled for current date
today_games = []

today_games.append(schedule[0])
for game in range(6, len(schedule), 6):
    today_games.append(schedule[game])


'''
#checks if player is playing today
for each_game in today_games:
    each_game = game.split()
    if city_name in each_game:
        for g in each_game:
            print g
    else:
        nop = False

if nop == False:
    print 'not playing'
'''



        





        
