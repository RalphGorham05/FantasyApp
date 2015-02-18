class Player:
    def __init__(self, name):
        self.name = name
        self.pid = ''
        self.team = ''
        self.stats = []


    #returns player espn id
    def get_pID(self, player, url):
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

        self.pid = pid


    def get_Stats(self, pid, table_num = 3):
        url = 'http://espn.go.com/nba/player/_/id/'
        url += str(pid)
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
            

        
