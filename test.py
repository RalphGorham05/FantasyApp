from mechanize import Browser
from bs4 import BeautifulSoup
from functions import *


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

urls = {}

for div in nba:
    for team in div:
        urls[team_Name(team)] = team

for k, v in urls.iteritems():
    print k, v



