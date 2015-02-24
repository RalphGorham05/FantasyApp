from bs4 import BeautifulSoup
from multiprocessing import Pool
import multiprocessing
import threading
from datetime import datetime, time
import re
from mechanize import Browser
#import peewee
#from peewee import *
import itertools
from functions import *



###########Program start#######################################################

#pl = raw_input('Enter player name: ')



#city_name = get_Team(pl, nba)
#print pl + ' plays for ' + city_name





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


total_teams = len(today_games) * 2
    #if city_name in games:
    for g in games:
        print g


        
        #print 'Defensive Rank \t Pace \t Ast \t Rebs \t Off Efficiency \t Def Efficiency'
        
        #s = get_teamStats(g)
        


'''

position_url = 'http://www.rotowire.com/daily/nba/defense-vspos.htm?site=DraftKings'

position_def = get_HTML_Table(position_url, 'table', 0)

#t_name = city_name.split()
#print t_name[1]

db = {}
position_stats = []
each_team = []
r = 0
q = 1

for r in range(r,len(position_def), 14):
    position_stats.append(position_def[r:r + 14])

for q in range(q, len(position_stats), 13):
    each_team.append(position_stats[q:q+13])
    
for p in position_stats:
    y = team_Name(p[0])
    print y



    t = p[0].split()
    t = t[len(t)-1]
    db[t] = p
    
    #print p


for k,v in db.iteritems():
    print k,v



    

nba_url = 'http://stats.nba.com/tracking/#!/player/possessions/'

possessions = get_HTML_Table(nba_url, 'table')

for p in possessions:
    print p


'''

'''
db = MySQLDatabase('fantasyApp', user='root', passwd='')


class BaseModel(Model):
    class Meta():
        database = db

class Teamsapo(BaseModel):
    team = CharField(default='')
    city = CharField(default='')
    abbr = CharField(default='')




#for t, c, a in itertools.izip(team_list, city_list, abr_list):
    #Teamsapo.create(team=t, city=c, abbr=a)



class BaseModel(Model):
    class Meta():
        database = db

class Players(BaseModel):
    name = CharField(default='')
    pid = IntegerField(default='')

'''
