from mechanize import Browser
from bs4 import BeautifulSoup

class Player:
    def __init__(self, name):
        self.name = name
        self.pid = ''
        self.team = ''
        self.stats = []


    city_list = []
team_list = []
abr_list = []
#check to find team
def get_Team(player, divs):
    tName = ''
    pdict = {}

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
            
            
            rows = playerTable.findChildren('tr')[2:]
            for row in rows:
                data = row.findChildren('td')
                name = data[1].text
               
                pi = get_pID(name, team)
                #pdict[name] = pi

                #for k, v in pdict.iteritems():
                    #print k,v 
                    #Players.create(name=k, pid=v)
                
                if player == name:
                    tName = city_Name(team)

    return tName


    #returns player espn id
    def get_pID(self, url):
        br = Browser()
        site = br.open(url)
        page = site.read()
        html = BeautifulSoup(page)
        table = html.find('table')
        links = table.findAll('a')
    
        for link in links:
            if self.name in link.text:
                sep = link.get('href').split('/')
                pid = sep[len(sep)-2]

        self.pid = pid


    def get_Stats(self, table_num = 3):
        url = 'http://espn.go.com/nba/player/_/id/'
        url += str(self.pid)
        br = Browser()
        site = br.open(url)
        page = site.read()
        html = BeautifulSoup(page)
        tables = html.findAll('table')

        stat_table = tables[table_num]

    
        rows = stat_table.findChildren('tr')[1:2]
        for row in rows:
            data = row.findChildren('td')[1:]
            name = data
            for n in name:
                self.stats.append(n)



p = Player('Brandon Bass')
p.get_pID('http://espn.go.com/nba/team/roster/_/name/bos/boston-celtics')
print p.pid

        
