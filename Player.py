from mechanize import Browser
from bs4 import BeautifulSoup
import functions



class Player:
    def __init__(self, name):
        self.name = name
        self.pid = ''
        self.team = ''
        self.stats = []



    #check to find team
    def get_Team(player):
        tName = ''

        for team in urls:
            page = str(team)
            code = process_Site(urls[page])
            playerTable = code.find('table')


            rows = playerTable.findChildren('tr')[2:]
            for row in rows:
                data = row.findChildren('td')
                name = data[1].text


                if player == name:
                    tName = city_Name(team)

        self.team = tName


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




