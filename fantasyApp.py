from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool
import multiprocessing
import threading
import time
import re
from mechanize import Browser

pl = raw_input('Enter player name: ')

#pool = Pool(8)


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




def team_Name(t):
    teamString = t.split('/')
    lastWord = len(teamString) - 1
    nameSeparated = teamString[lastWord].split('-')
    city = nameSeparated[0]

    return city

#check to find team
def get_Team(player,divs):
    for division in divs:
        for team in division:
            t = requests.get(team)
            soup = BeautifulSoup(t.text)
            link = soup.select('td.sortcell')
            for a in link:
                #print a.find('a')['href']
                if (player in a.find('a').contents[0]):
                    f = team_Name(team)
                    
    return f

start = time.clock()
#w = get_Team(pl,nba);
#print w
end = time.clock()
#print end - start



u = 'http://espn.go.com/nba/hollinger/teamstats/_/sort/defensiveEff/order/false'
mech = Browser()
page = mech.open(u)
html = page.read()
msoup = BeautifulSoup(html)
table = msoup.find("table")


st = []
rows = table.findChildren('tr')[2:]
for row in rows:
     cells = row.findChildren('td')
     for cell in cells:
         value = cell.text
         st.append(value)
         #print "The value in this cell is %s" % value
print st[:12]

'''
for row in table.findAll('tr')[2:]:
    col = row.findAll('td')
    tRank = col[0].text
    tCities = col[1].text
    tPace = col[2].text
    tAsts = col[3].text
    tRebR = col[7].text
    tOff = col[10].text
    tDef = col[11].text

    tStats = (tRank, tCities, tPace, tAsts, tRebR, tOff, tDef)

    print "|".join(tStats)
    
 '''   

'''
odd = []
even = []
tree = BeautifulSoup(up.text)

for node in tree.findAll(attrs={'class': re.compile(r".*\evenrow\b.*")}):
    even.append(node)
for node in tree.findAll(attrs={'tr': re.compile(r".*\oddrow\b.*")}):
    odd.append(node)

team_Data = {}

for o in odd:
    #p = o.find('a').contents[0]
    data = o.find('a')
    
    #for d in data:
        #print d.text
    cityNames = o.findAll('td')[1].text
    if (w or w.upper() in cityNames):
        print data
'''



  

    



'''
class myThread (threading.Thread):
    def __init__(self, threadID, player, league):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.player = player
        self.league = league
        
    def run(self):
        print "Starting " + self.name
        get_Team(self.player,self.league)
        print "Exiting " + self.name



# Create new threads
thread1 = myThread(1, "Thread-1", 1,pl,nba)
thread2 = myThread(2, "Thread-2", 2,pl,nba)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"

'''


'''
class Fantasy:
    def __init__(self,p):
        self.player = p

    def getPlayerTeam(pl):
        self.team = 'Duke'
        return self.team




test = Fantasy(pl)
print test.player
'''


