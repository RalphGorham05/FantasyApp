from mechanize import Browser
from bs4 import BeautifulSoup


pid = 2745


def get_playerStats(pid):
    url = 'http://espn.go.com/nba/player/_/id/'
    url += str(pid)
    br = Browser()
    site = br.open(url)
    page = site.read()
    html = BeautifulSoup(page)
    tables = html.findAll('table')

    stats = tables[3]

    
    rows = stats.findChildren('tr')[1:2]
    for row in rows:
        data = row.findChildren('td')[1:]
        name = data
        for n in name:
            print n.text



get_s(2745)

   
    
        
    

