from datetime import datetime, time
import re
from mechanize import Browser
from bs4 import BeautifulSoup
import peewee
from peewee import *
import itertools



db = MySQLDatabase('fantasyApp', user='root', passwd='')


#for t, c, a in itertools.izip(team_list, city_list, abr_list):
    #Teamsapo.create(team=t, city=c, abbr=a)



class BaseModel(Model):
    class Meta():
        database = db

class Players(BaseModel):
    name = CharField(default='')
    pid = IntegerField(default='')





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




city_list = []
team_list = []
abr_list = []
#check to find team
def get_Team(player, divs):
    tName = ''
    for division in divs:
        for team in division:
            code = process_Site(team)
            playerTable = code.find('table')
            

            #make list of all the cities
            city_list.append(city_Name(team))
            #make list of all the team
            team_list.append(team_Name(team))
            #make list of abbrs
            abr_list.append(city_Abbr(team))
            
            
            pdict = {}
            rows = playerTable.findChildren('tr')[2:]
            for row in rows:
                data = row.findChildren('td')
                name = data[1].text
                pi = get_pID(name, team)
                pdict[name] = pi

                for k, v in pdict.iteritems():
                    Players.create(name=k, pid=v)
                if player == name:
                    tName = city_Name(team)

    return tName




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
