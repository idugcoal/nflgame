import nflgame

choice = raw_input("what team? ")

team = nflgame.standard_team(choice)

games = nflgame.games(2014, home=team, away=team)

players = nflgame.combine_game_stats(games)

for p in players.passing().sort('passing_yds'):
	print p.team, p, p.passing_yds