"""
@author: daviddeepwell
"""

def team_list(year, rnd):
    # create the list of the teams in the current round
    
    import pandas as pd
    
    # read data
    fname = str(year)+' Friendly Playoff Pool Round '+str(rnd)+'.csv'    # read file
    fdata = pd.read_csv(fname, sep=',')
    header = fdata.columns.values
    
    # find the header containing the teams in each round
    if rnd == 1:
        team_series = header[2:-3:2]
    else:
        team_series = header[2::2]
    
    # separate into different team strings
    teams = []
    for matchup in team_series:
        teams.extend(matchup.split('-'))
    teams_west = teams[:len(teams)//2]
    teams_east = teams[len(teams)//2:]
    
    return teams_west, teams_east

def shorten_team_name_city( team ):
    #Shorten the team name into it's acronym
    if team == 'Anaheim Ducks':
        return 'Anaheim'
    elif team == 'Arizona Coyotes':
        return 'Arizona'
    elif team == 'Boston Bruins':
        return 'Boston'
    elif team == 'Buffalo Sabres':
        return 'Buffalo'
    elif team == 'Calgary Flames':
        return 'Calgary'
    elif team == 'Carolina Hurricanes':
        return 'Carolina'
    elif team == 'Chicago Blackhawks':
        return 'Chicago'
    elif team == 'Colorado Avalanche':
        return 'Colorado'
    elif team == 'Columbus Blue Jackets':
        return 'Columbus'
    elif team == 'Dallas Stars':
        return 'Dallas'
    elif team == 'Detroit Red Wings':
        return 'Detroit'
    elif team == 'Edmonton Oilers':
        return 'Edmonton'
    elif team == 'Florida Panthers':
        return 'Florida'
    elif team == 'Los Angeles Kings':
        return 'Los Angeles'
    elif team == 'Minnesota Wild':
        return 'Minnesota'
    elif team == 'Montreal Canadiens':
        return 'Montreal'
    elif team == 'Nashville Predators':
        return 'Nashville'
    elif team == 'New Jersey Devils':
        return 'New Jersey'
    elif team == 'New York Islanders':
        return 'NY Islanders'
    elif team == 'New York Rangers':
        return 'NY Rangers'
    elif team == 'Ottawa Senators':
        return 'Ottawa'
    elif team == 'Philadelphia Flyers':
        return 'Philadelphia'
    elif team == 'Pittsburgh Penguins':
        return 'Pittsburgh'
    elif team == 'San Jose Sharks':
        return 'San Jose'
    elif team == 'St. Louis Blues':
        return 'St Louis'
    elif team == 'Tampa Bay Lightning':
        return 'Tampa Bay'
    elif team == 'Toronto Maple Leafs':
        return 'Toronto'
    elif team == 'Vancouver Canucks':
        return 'Vancouver'
    elif team == 'Vegas Golden Knights':
        return 'Vegas'
    elif team == 'Washington Capitals':
        return 'Washington'
    elif team == 'Winnipeg Jets':
        return 'Winnipeg'

def shorten_team_name_acronym( team ):
    #Shorten the team name into it's acronym
    if team == 'Anaheim Ducks':
        return 'ANA'
    elif team == 'Arizona Coyotes':
        return 'ARI'
    elif team == 'Boston Bruins':
        return 'BOS'
    elif team == 'Buffalo Sabres':
        return 'BUF'
    elif team == 'Calgary Flames':
        return 'CGY'
    elif team == 'Carolina Hurricanes':
        return 'CAR'
    elif team == 'Chicago Blackhawks':
        return 'CHI'
    elif team == 'Colorado Avalanche':
        return 'COL'
    elif team == 'Columbus Blue Jackets':
        return 'CBJ'
    elif team == 'Dallas Stars':
        return 'DAL'
    elif team == 'Detroit Red Wings':
        return 'DET'
    elif team == 'Edmonton Oilers':
        return 'EDM'
    elif team == 'Florida Panthers':
        return 'FLA'
    elif team == 'Los Angeles Kings':
        return 'LAK'
    elif team == 'Minnesota Wild':
        return 'MIN'
    elif team == 'Montreal Canadiens':
        return 'MTL'
    elif team == 'Nashville Predators':
        return 'NSH'
    elif team == 'New Jersey Devils':
        return 'NJD'
    elif team == 'New York Islanders':
        return 'NYI'
    elif team == 'New York Rangers':
        return 'NYR'
    elif team == 'Ottawa Senators':
        return 'OTT'
    elif team == 'Philadelphia Flyers':
        return 'PHI'
    elif team == 'Pittsburgh Penguins':
        return 'PIT'
    elif team == 'San Jose Sharks':
        return 'SJS'
    elif team == 'St Louis Blues':
        return 'STL'
    elif team == 'Tampa Bay Lightning':
        return 'TBL'
    elif team == 'Toronto Maple Leafs':
        return 'TOR'
    elif team == 'Vancouver Canucks':
        return 'VAN'
    elif team == 'Vegas Golden Knights':
        return 'VGK'
    elif team == 'Washington Capitals':
        return 'WSH'
    elif team == 'Winnipeg Jets':
        return 'WPG'
    
def lengthen_team_name_acronym( team ):
    #lengthen the team name from it's acronym
    if team == 'ANA':
        return 'Anaheim Ducks'
    elif team == 'ARI':
        return 'Arizona Coyotes'
    elif team == 'BOS':
        return 'Boston Bruins'
    elif team == 'BUF':
        return 'Buffalo Sabres'
    elif team == 'CGY':
        return 'Calgary Flames'
    elif team == 'CAR':
        return 'Carolina Hurricanes'
    elif team == 'CHI':
        return 'Chicago Blackhawks'
    elif team == 'COL':
        return 'Colorado Avalanche'
    elif team == 'CBJ':
        return 'Columbus Blue Jackets'
    elif team == 'DAL':
        return 'Dallas Stars'
    elif team == 'DET':
        return 'Detroit Red Wings'
    elif team == 'EDM':
        return 'Edmonton Oilers'
    elif team == 'FLA':
        return 'Florida Panthers'
    elif team == 'LAK':
        return 'Los Angeles Kings'
    elif team == 'MIN':
        return 'Minnesota Wild'
    elif team == 'MTL':
        return 'Montreal Canadiens'
    elif team == 'NSH':
        return 'Nashville Predators'
    elif team == 'NJD':
        return 'New Jersey Devils'
    elif team == 'NYI':
        return 'New York Islanders'
    elif team == 'NYR':
        return 'New York Rangers'
    elif team == 'OTT':
        return 'Ottawa Senators'
    elif team == 'PHI':
        return 'Philadelphia Flyers'
    elif team == 'PIT':
        return 'Pittsburgh Penguins'
    elif team == 'SJS':
        return 'San Jose Sharks'
    elif team == 'STL':
        return 'St Louis Blues'
    elif team == 'TBL':
        return 'Tampa Bay Lightning'
    elif team == 'TOR':
        return 'Toronto Maple Leafs'
    elif team == 'VAN':
        return 'Vancouver Canucks'
    elif team == 'VGK':
        return 'Vegas Golden Knights'
    elif team == 'WSH':
        return 'Washington Capitals'
    elif team == 'WPG':
        return 'Winnipeg Jets'