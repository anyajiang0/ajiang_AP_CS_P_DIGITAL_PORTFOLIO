"""
THIS IS A SIMULATION, THERE IS *NO* REAL MONEY INVOLVED.
THIS SIMULATION IS NOT INTENDED TO ENCOURAGE GAMBLING IN ANY WAY, SHAPE, OR FORM.
"""
# imports 

import math

TEAMS = {
    "OKC": {"name": "Oklahoma City Thunder", "wins": 51, "losses": 15, "ppg": 120.4, "oppg": 108.1, "home_plusminus": 14.8, "road_plusminus": 9.6,  "last5": [1,1,1,1,0]},
    "SAS": {"name": "San Antonio Spurs", "wins": 48, "losses": 17, "ppg": 118.2, "oppg": 110.3, "home_plusminus": 12.4, "road_plusminus": 6.8,  "last5": [1,1,1,0,1]},
    "DET": {"name": "Detroit Pistons", "wins": 46, "losses": 18, "ppg": 116.8, "oppg": 109.5, "home_plusminus": 11.9, "road_plusminus": 5.4,  "last5": [1,1,1,1,1]},
    "BOS": {"name": "Boston Celtics", "wins": 43, "losses": 22, "ppg": 119.5, "oppg": 112.4, "home_plusminus": 10.2, "road_plusminus": 5.8,  "last5": [0,1,0,1,0]},
    "NYK": {"name": "New York Knicks", "wins": 42, "losses": 25, "ppg": 114.7, "oppg": 109.8, "home_plusminus": 8.4,  "road_plusminus": 2.6,  "last5": [0,1,1,0,1]},
    "LAL": {"name": "Los Angeles Lakers", "wins": 40, "losses": 25, "ppg": 115.6, "oppg": 111.2, "home_plusminus": 7.8,  "road_plusminus": 3.1,  "last5": [1,1,0,1,1]},
    "HOU": {"name": "Houston Rockets", "wins": 40, "losses": 25, "ppg": 112.9, "oppg": 108.7, "home_plusminus": 8.9,  "road_plusminus": 3.4,  "last5": [1,0,1,1,0]},
    "DEN": {"name": "Denver Nuggets", "wins": 40, "losses": 26, "ppg": 116.3, "oppg": 113.1, "home_plusminus": 9.6,  "road_plusminus": 1.8,  "last5": [1,0,1,1,0]},
    "MIN": {"name": "Minnesota Timberwolves", "wins": 40, "losses": 26, "ppg": 113.6, "oppg": 109.4, "home_plusminus": 8.2,  "road_plusminus": 2.6,  "last5": [0,1,1,0,0]},
    "CLE": {"name": "Cleveland Cavaliers", "wins": 40, "losses": 26, "ppg": 113.8, "oppg": 108.4, "home_plusminus": 9.1,  "road_plusminus": 3.7,  "last5": [0,1,0,1,0]},
    "PHX": {"name": "Phoenix Suns", "wins": 38, "losses": 27, "ppg": 114.2, "oppg": 112.0, "home_plusminus": 6.4,  "road_plusminus": 0.9,  "last5": [1,1,0,1,0]},
    "MIA": {"name": "Miami Heat", "wins": 37, "losses": 29, "ppg": 115.1, "oppg": 112.8, "home_plusminus": 7.2,  "road_plusminus": 1.4,  "last5": [1,0,1,1,0]},
    "ORL": {"name": "Orlando Magic", "wins": 36, "losses": 28, "ppg": 110.4, "oppg": 106.9, "home_plusminus": 7.8,  "road_plusminus": 1.2,  "last5": [1,0,1,0,1]},
    "TOR": {"name": "Toronto Raptors", "wins": 36, "losses": 29, "ppg": 112.3, "oppg": 112.1, "home_plusminus": 4.1,  "road_plusminus": -0.8, "last5": [0,0,0,1,0]},
    "PHI": {"name": "Philadelphia 76ers", "wins": 35, "losses": 30, "ppg": 114.6, "oppg": 114.0, "home_plusminus": 5.2,  "road_plusminus": -0.4, "last5": [1,0,1,0,0]},
    "ATL": {"name": "Atlanta Hawks", "wins": 34, "losses": 31, "ppg": 117.2, "oppg": 116.5, "home_plusminus": 4.8,  "road_plusminus": -0.2, "last5": [1,0,0,1,0]},
    "CHA": {"name": "Charlotte Hornets", "wins": 34, "losses": 33, "ppg": 113.5, "oppg": 113.8, "home_plusminus": 3.8,  "road_plusminus": -2.1, "last5": [1,0,1,0,1]},
    "LAC": {"name": "LA Clippers", "wins": 33, "losses": 32, "ppg": 114.8, "oppg": 114.1, "home_plusminus": 4.4,  "road_plusminus": -1.6, "last5": [1,0,1,0,1]},
    "GSW": {"name": "Golden State Warriors", "wins": 32, "losses": 33, "ppg": 113.4, "oppg": 112.9, "home_plusminus": 5.1,  "road_plusminus": -2.4, "last5": [0,0,1,1,0]},
    "POR": {"name": "Portland Trail Blazers", "wins": 31, "losses": 35, "ppg": 111.6, "oppg": 114.2, "home_plusminus": 1.8,  "road_plusminus": -5.4, "last5": [0,1,0,0,1]},
    "CHI": {"name": "Chicago Bulls", "wins": 27, "losses": 38, "ppg": 112.1, "oppg": 114.7, "home_plusminus": 0.6,  "road_plusminus": -4.8, "last5": [1,0,0,0,1]},
    "MIL": {"name": "Milwaukee Bucks", "wins": 27, "losses": 37, "ppg": 111.8, "oppg": 114.9, "home_plusminus": -0.4, "road_plusminus": -5.2, "last5": [0,1,0,0,0]},
    "MEM": {"name": "Memphis Grizzlies", "wins": 23, "losses": 41, "ppg": 110.2, "oppg": 116.3, "home_plusminus": -2.1, "road_plusminus": -8.4, "last5": [0,0,1,0,0]},
    "NOP": {"name": "New Orleans Pelicans", "wins": 22, "losses": 45, "ppg": 109.1, "oppg": 116.8, "home_plusminus": -4.2, "road_plusminus": -9.8, "last5": [1,0,0,0,0]},
    "DAL": {"name": "Dallas Mavericks", "wins": 21, "losses": 44, "ppg": 108.8, "oppg": 116.2, "home_plusminus": -4.8, "road_plusminus":-10.2, "last5": [1,0,0,0,0]},
    "UTA": {"name": "Utah Jazz", "wins": 20, "losses": 46, "ppg": 109.7, "oppg": 118.4, "home_plusminus": -5.4, "road_plusminus":-12.1, "last5": [1,0,0,0,0]},
    "WAS": {"name": "Washington Wizards", "wins": 16, "losses": 48, "ppg": 108.9, "oppg": 119.6, "home_plusminus": -7.1, "road_plusminus":-13.8, "last5": [0,0,0,0,0]},
    "BKN": {"name": "Brooklyn Nets", "wins": 17, "losses": 48, "ppg": 108.3, "oppg": 118.7, "home_plusminus": -6.8, "road_plusminus":-13.2, "last5": [1,0,0,0,0]},
    "IND": {"name": "Indiana Pacers", "wins": 15, "losses": 50, "ppg": 108.4, "oppg": 119.3, "home_plusminus": -7.4, "road_plusminus":-14.1, "last5": [0,0,0,1,0]},
    "SAC": {"name": "Sacramento Kings", "wins": 16, "losses": 51, "ppg": 110.1, "oppg": 119.8, "home_plusminus": -5.8, "road_plusminus":-13.4, "last5": [1,1,0,0,0]},
}


def team_power_rating(team):
    games_played = team["wins"] + team["losses"]
    win_percentage = team["wins"] / games_played
    point_differential = team["ppg"] - team ["oppg"]
    streak = sum(team["last5"]) / 5 
    return (win_percentage * 5.0) + (point_differential * 0.14) + (streak * 0.65)

def away_factor(team):
    """
    Compares road point margins to overall point differences
    A factor less than 1.0 means they're worse away
    A factor greater than 1.0 means they're better away
    Rated on a scale between 0.5 and 1.5 
    """
    overall_difference = team["ppg"] - team["oppg"]
    if abs(overall_difference) < 0.5:
        return 1.0 # neutral, no meaningful adjustment
    else:
        return max(0.5, min(1.5, team["road_plusminus"] / overall_difference))
    
def away_rating(team):
    games_played = team["wins"] + team["losses"]
    win_percentage = team["wins"] / games_played
    point_differential = team["ppg"] - team ["oppg"]
    streak = sum(team["last5"]) / 5
    road_adjustment = away_factor(team)
    return ((win_percentage * 30) + (point_differential * road_adjustment * 1.5) + (streak * 15))

home_court_advantage = 3.0

def calc_spread(home_team, away_team):
    home_rating = team_power_rating(home_team)
    away_team_rating = away_rating(away_team)
    hca = home_court_advantage
    raw = home_rating - away_team_rating + hca 
    spread = round(raw * 2) / 2
    return spread, home_rating, away_team_rating, hca, raw

def spread_to_moneyline(spread):
    """
    Creating ***FAKE*** American moneyline odds from the spread
    k = 0.04

    Implied probability: P = 1 / (1 + e^(-k * spread))
    Favorite odds: -(probability / (1 - probability)) * 100
    Underdog odds: ((1 - probability) / probability) * 100
    """

    k = 0.04  # Keep as float, NOT int
    home_probability = 1 / (1 + math.exp(-k * spread))
    away_probability = 1 - home_probability

    def to_moneyline(probability):
        if probability >= 0.5: # greater than 50%
            return -round((probability / (1 - probability)) * 100) # negative odds for favorites
        else:
            return +round(((1 - probability) / probability) * 100) # positive odds for underdogs

    return {
        "home_ml": to_moneyline(home_probability),
        "away_ml": to_moneyline(away_probability),
        "home_prob": round(home_probability * 100, 1),
        "away_prob": round(away_probability * 100, 1),
    }

def print_result(home_team, away_team): 
    home = TEAMS[home_team]
    away = TEAMS[away_team]
    spread, home_rating, away_rating, hca, raw = calc_spread(home, away)
    odds = spread_to_moneyline(spread)

    print(f"{home['name']} vs. {away['name']}")
    print(f"Spread: {spread}")
    print(f"Home Moneyline ({home['name']}): {odds['home_ml']}")
    print(f"Away Moneyline ({away['name']}): {odds['away_ml']}")
    print(f"Odds: {home['name']} {odds['home_prob']}% | {away['name']} {odds['away_prob']}%")

class Candy: 
    def __init__(self, starting_candies = 1000): 
        self.balance = starting_candies
        self.total_won = 0
        self.total_lost = 0

    def place_bet(self, amount, odds, bet_amount, team_name, won=None): 
        if bet_amount > self.balance:
            return "Not enough candies to place bet, try again"
        self.balance -= bet_amount
        bet = {
            "team" : team_name, 

        }

def main():
    
    while True:
        print("1. Pick your own matchup")
        print("2. Quick example (BOS vs. NYK)")
        print("3. Exit")
        choice = input("Pick a number 1-3: ")

        if choice == "1": 
            home_team = "BKN"
            away_team = "BOS"
            print_result(home_team, away_team)

if __name__ == "__main__":
    main()

    
    






    
"""
THIS IS A SIMULATION, THERE IS *NO* REAL MONEY INVOLVED.
THIS SIMULATION IS NOT INTENDED TO ENCOURAGE GAMBLING IN ANY WAY, SHAPE, OR FORM.
"""
# imports 

import math

TEAMS = {
    "OKC": {"name": "Oklahoma City Thunder", "wins": 51, "losses": 15, "ppg": 120.4, "oppg": 108.1, "home_plusminus": 14.8, "road_plusminus": 9.6,  "last5": [1,1,1,1,0]},
    "SAS": {"name": "San Antonio Spurs", "wins": 48, "losses": 17, "ppg": 118.2, "oppg": 110.3, "home_plusminus": 12.4, "road_plusminus": 6.8,  "last5": [1,1,1,0,1]},
    "DET": {"name": "Detroit Pistons", "wins": 46, "losses": 18, "ppg": 116.8, "oppg": 109.5, "home_plusminus": 11.9, "road_plusminus": 5.4,  "last5": [1,1,1,1,1]},
    "BOS": {"name": "Boston Celtics", "wins": 43, "losses": 22, "ppg": 119.5, "oppg": 112.4, "home_plusminus": 10.2, "road_plusminus": 5.8,  "last5": [0,1,0,1,0]},
    "NYK": {"name": "New York Knicks", "wins": 42, "losses": 25, "ppg": 114.7, "oppg": 109.8, "home_plusminus": 8.4,  "road_plusminus": 2.6,  "last5": [0,1,1,0,1]},
    "LAL": {"name": "Los Angeles Lakers", "wins": 40, "losses": 25, "ppg": 115.6, "oppg": 111.2, "home_plusminus": 7.8,  "road_plusminus": 3.1,  "last5": [1,1,0,1,1]},
    "HOU": {"name": "Houston Rockets", "wins": 40, "losses": 25, "ppg": 112.9, "oppg": 108.7, "home_plusminus": 8.9,  "road_plusminus": 3.4,  "last5": [1,0,1,1,0]},
    "DEN": {"name": "Denver Nuggets", "wins": 40, "losses": 26, "ppg": 116.3, "oppg": 113.1, "home_plusminus": 9.6,  "road_plusminus": 1.8,  "last5": [1,0,1,1,0]},
    "MIN": {"name": "Minnesota Timberwolves", "wins": 40, "losses": 26, "ppg": 113.6, "oppg": 109.4, "home_plusminus": 8.2,  "road_plusminus": 2.6,  "last5": [0,1,1,0,0]},
    "CLE": {"name": "Cleveland Cavaliers", "wins": 40, "losses": 26, "ppg": 113.8, "oppg": 108.4, "home_plusminus": 9.1,  "road_plusminus": 3.7,  "last5": [0,1,0,1,0]},
    "PHX": {"name": "Phoenix Suns", "wins": 38, "losses": 27, "ppg": 114.2, "oppg": 112.0, "home_plusminus": 6.4,  "road_plusminus": 0.9,  "last5": [1,1,0,1,0]},
    "MIA": {"name": "Miami Heat", "wins": 37, "losses": 29, "ppg": 115.1, "oppg": 112.8, "home_plusminus": 7.2,  "road_plusminus": 1.4,  "last5": [1,0,1,1,0]},
    "ORL": {"name": "Orlando Magic", "wins": 36, "losses": 28, "ppg": 110.4, "oppg": 106.9, "home_plusminus": 7.8,  "road_plusminus": 1.2,  "last5": [1,0,1,0,1]},
    "TOR": {"name": "Toronto Raptors", "wins": 36, "losses": 29, "ppg": 112.3, "oppg": 112.1, "home_plusminus": 4.1,  "road_plusminus": -0.8, "last5": [0,0,0,1,0]},
    "PHI": {"name": "Philadelphia 76ers", "wins": 35, "losses": 30, "ppg": 114.6, "oppg": 114.0, "home_plusminus": 5.2,  "road_plusminus": -0.4, "last5": [1,0,1,0,0]},
    "ATL": {"name": "Atlanta Hawks", "wins": 34, "losses": 31, "ppg": 117.2, "oppg": 116.5, "home_plusminus": 4.8,  "road_plusminus": -0.2, "last5": [1,0,0,1,0]},
    "CHA": {"name": "Charlotte Hornets", "wins": 34, "losses": 33, "ppg": 113.5, "oppg": 113.8, "home_plusminus": 3.8,  "road_plusminus": -2.1, "last5": [1,0,1,0,1]},
    "LAC": {"name": "LA Clippers", "wins": 33, "losses": 32, "ppg": 114.8, "oppg": 114.1, "home_plusminus": 4.4,  "road_plusminus": -1.6, "last5": [1,0,1,0,1]},
    "GSW": {"name": "Golden State Warriors", "wins": 32, "losses": 33, "ppg": 113.4, "oppg": 112.9, "home_plusminus": 5.1,  "road_plusminus": -2.4, "last5": [0,0,1,1,0]},
    "POR": {"name": "Portland Trail Blazers", "wins": 31, "losses": 35, "ppg": 111.6, "oppg": 114.2, "home_plusminus": 1.8,  "road_plusminus": -5.4, "last5": [0,1,0,0,1]},
    "CHI": {"name": "Chicago Bulls", "wins": 27, "losses": 38, "ppg": 112.1, "oppg": 114.7, "home_plusminus": 0.6,  "road_plusminus": -4.8, "last5": [1,0,0,0,1]},
    "MIL": {"name": "Milwaukee Bucks", "wins": 27, "losses": 37, "ppg": 111.8, "oppg": 114.9, "home_plusminus": -0.4, "road_plusminus": -5.2, "last5": [0,1,0,0,0]},
    "MEM": {"name": "Memphis Grizzlies", "wins": 23, "losses": 41, "ppg": 110.2, "oppg": 116.3, "home_plusminus": -2.1, "road_plusminus": -8.4, "last5": [0,0,1,0,0]},
    "NOP": {"name": "New Orleans Pelicans", "wins": 22, "losses": 45, "ppg": 109.1, "oppg": 116.8, "home_plusminus": -4.2, "road_plusminus": -9.8, "last5": [1,0,0,0,0]},
    "DAL": {"name": "Dallas Mavericks", "wins": 21, "losses": 44, "ppg": 108.8, "oppg": 116.2, "home_plusminus": -4.8, "road_plusminus":-10.2, "last5": [1,0,0,0,0]},
    "UTA": {"name": "Utah Jazz", "wins": 20, "losses": 46, "ppg": 109.7, "oppg": 118.4, "home_plusminus": -5.4, "road_plusminus":-12.1, "last5": [1,0,0,0,0]},
    "WAS": {"name": "Washington Wizards", "wins": 16, "losses": 48, "ppg": 108.9, "oppg": 119.6, "home_plusminus": -7.1, "road_plusminus":-13.8, "last5": [0,0,0,0,0]},
    "BKN": {"name": "Brooklyn Nets", "wins": 17, "losses": 48, "ppg": 108.3, "oppg": 118.7, "home_plusminus": -6.8, "road_plusminus":-13.2, "last5": [1,0,0,0,0]},
    "IND": {"name": "Indiana Pacers", "wins": 15, "losses": 50, "ppg": 108.4, "oppg": 119.3, "home_plusminus": -7.4, "road_plusminus":-14.1, "last5": [0,0,0,1,0]},
    "SAC": {"name": "Sacramento Kings", "wins": 16, "losses": 51, "ppg": 110.1, "oppg": 119.8, "home_plusminus": -5.8, "road_plusminus":-13.4, "last5": [1,1,0,0,0]},
}


def team_power_rating(team):
    games_played = team["wins"] + team["losses"]
    win_percentage = team["wins"] / games_played
    point_differential = team["ppg"] - team ["oppg"]
    streak = sum(team["last5"]) / 5 
    return (win_percentage * 4) + (point_differential * 0.1) + (streak * 0.5)

def away_factor(team):
    """
    Compares road point margins to overall point differences
    A factor less than 1.0 means they're worse away
    A factor greater than 1.0 means they're better away
    Rated on a scale between 0.5 and 1.5 
    """
    overall_difference = team["ppg"] - team["oppg"]
    if abs(overall_difference) < 0.5:
        return 1.0 # neutral, no meaningful adjustment
    else:
        return max(0.5, min(1.5, team["road_plusminus"] / overall_difference))
    
def away_rating(team):
    games_played = team["wins"] + team["losses"]
    win_percentage = team["wins"] / games_played
    point_differential = team["ppg"] - team ["oppg"]
    streak = sum(team["last5"]) / 5
    road_adjustment = away_factor(team)
    return ((win_percentage * 30) + (point_differential * road_adjustment * 1.5) + (streak * 15))

home_court_advantage = 3.0

def calc_spread(home_team, away_team):
    home_rating = team_power_rating(home_team)
    away_team_rating = away_rating(away_team)
    hca = home_court_advantage
    raw = home_rating - away_team_rating + hca 
    spread = round(raw * 2) / 2
    return spread, home_rating, away_team_rating, hca, raw

def spread_to_moneyline(spread):
    """
    Creating ***FAKE*** American moneyline odds from the spread
    k = 0.04

    Implied probability: P = 1 / (1 + e^(-k * spread))
    Favorite odds: -(probability / (1 - probability)) * 100
    Underdog odds: ((1 - probability) / probability) * 100
    """

    k = 0.04  # Keep as float, NOT int
    home_probability = 1 / (1 + math.exp(-k * spread))
    away_probability = 1 - home_probability

    def to_moneyline(probability):
        if probability >= 0.5: # greater than 50%
            return -round((probability / (1 - probability)) * 100) # negative odds for favorites
        else:
            return +round(((1 - probability) / probability) * 100) # positive odds for underdogs

    return {
        "home_ml": to_moneyline(home_probability),
        "away_ml": to_moneyline(away_probability),
        "home_prob": round(home_probability * 100, 1),
        "away_prob": round(away_probability * 100, 1),
    }

def print_result(home_team, away_team): 
    home = TEAMS[home_team]
    away = TEAMS[away_team]
    spread, home_rating, away_rating, hca, raw = calc_spread(home, away)
    odds = spread_to_moneyline(spread)

    print(f"{home['name']} vs. {away['name']}")
    print(f"Spread: {spread}")
    print(f"Home Moneyline ({home['name']}): {odds['home_ml']}")
    print(f"Away Moneyline ({away['name']}): {odds['away_ml']}")
    print(f"Odds: {home['name']} {odds['home_prob']}% | {away['name']} {odds['away_prob']}%")

class Candy: 
    def __init__(self, starting_candies = 1000): 
        self.balance = starting_candies
        self.total_won = 0
        self.total_lost = 0

    def place_bet(self, amount, odds, bet_amount, team_name, won=None): 
        if bet_amount > self.balance:
            return "Not enough candies to place bet, try again"
        self.balance -= bet_amount
        bet = {
            "team" : team_name, 

        }

def main():
    
    while True:
        print("1. Pick your own matchup")
        print("2. Quick example (BOS vs. NYK)")
        print("3. Exit")
        choice = input("Pick a number 1-3: ")

        if choice == "1": 
            home_team = "BKN"
            away_team = "BOS"
            print_result(home_team, away_team)

if __name__ == "__main__":
    main()

    
    






    