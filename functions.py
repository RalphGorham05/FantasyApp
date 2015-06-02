from datetime import datetime, time
import re
from mechanize import Browser
from bs4 import BeautifulSoup
#import peewee
#from peewee import *
import itertools


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


########################################


'''
db = MySQLDatabase('fantasyApp', user='root', passwd='')


#for t, c, a in itertools.izip(team_list, city_list, abr_list):
    #Teamsapo.create(team=t, city=c, abbr=a)



class BaseModel(Model):
    class Meta():
        database = db

class Players(BaseModel):
    name = CharField(default='')
    pid = IntegerField(default='')
'''


def get_playerStats(pid, table_num = 3):
    url = 'http://espn.go.com/nba/player/_/id/'
    url += str(pid)
    br = Browser()
    site = br.open(url)
    page = site.read()
    html = BeautifulSoup(page)
    tables = html.findAll('table')

    stats = tables[table_num]

    
    rows = stats.findChildren('tr')[1:2]
    for row in rows:
        data = row.findChildren('td')[1:]
        name = data
        for n in name:
            print n.text
            

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

    #print('\t '.join(map(str, stats)))
    return ('\t '.join(map(str, stats)))


    
    

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
def get_HTML_Table(url, data, table_number):
    processed = process_Site(url)
    data_table = processed.findAll(data)[table_number]
    table = parse_Table(data_table)

    return table


#splits the Team string to get only the city name
def city_Name(e):
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

#gets team name
def city_Abbr(e):
    teamString = e.split('/')
    spot = len(teamString) - 2
    ab = teamString[spot]

    return ab

#gets abbreviation
def team_Name(e):
    teamString = e.split('/')
    lastWord = len(teamString) - 1
    nameSeparated = teamString[lastWord].split('-')
    whole = len(nameSeparated)

    team = nameSeparated[whole - 1]

    return team

urls = {}

for div in nba:
    for team in div:
        urls[team_Name(team)] = team
    

city_list = []
team_list = []
abr_list = []
#check to find team
def get_Team(player):
    tName = ''
    pdict = {}

    
    for team in urls:
        page = str(team)
        code = process_Site(urls[page])
        playerTable = code.find('table')
            

        #make list of all the cities
        city_list.append(city_Name(team))
        #make list of all the team
        team_list.append(team_Name(team))
        #make list of abbrs
        abr_list.append(city_Abbr(team))
            
            
        rows = playerTable.findChildren('tr')[2:]
        for row in rows:
            data = row.findChildren('td')
            name = data[1].text
                   
            #pi = get_pID(name, team)
            #pdict[name] = pi

            #for k, v in pdict.iteritems():
                #print k,v 
                #Players.create(name=k, pid=v)
                    
            if player == name:
                tName = city_Name(team)

    return tName


#get_Team('James Harden')

#gets ESPN player id
def get_pID(player, url):
    br = Browser()
    site = br.open(url)
    page = site.read()
    html = BeautifulSoup(page)
    table = html.find('table')
    links = table.findAll('a')
    
    for link in links:
        if player in link.text:
            sep = link.get('href').split('/')
            pid = sep[len(sep)-2]

    return pid

#gets list of players on team
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

