require 'mechanize'


 url = 'http://stats.nba.com/team/#!/1610612752/players/'
br = Mechanize.new
html = br.get(url)



class Player
	def initialize(name)
		@name = name
		@stats = []
		@pid = ''
	end

end

player = Player. new('John Barry')
puts player

