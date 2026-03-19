import math

# ─────────────────────────────────────────────────────────────────────────────
# 2025-26 NBA TEAM DATA
# ppg/oppg = points per game for/against
# home_pm/road_pm = avg point margin at home vs on the road
# last5 = last 5 results as 1 (win) or 0 (loss), most recent first
# ─────────────────────────────────────────────────────────────────────────────
TEAMS = {
    "OKC": {"name": "Oklahoma City Thunder", "wins": 51, "losses": 15, "ppg": 120.4, "oppg": 108.1, "home_pm": 14.8, "road_pm": 9.6,  "last5": [1,1,1,1,0]},
    "SAS": {"name": "San Antonio Spurs",     "wins": 48, "losses": 17, "ppg": 118.2, "oppg": 110.3, "home_pm": 12.4, "road_pm": 6.8,  "last5": [1,1,1,0,1]},
    "DET": {"name": "Detroit Pistons",        "wins": 46, "losses": 18, "ppg": 116.8, "oppg": 109.5, "home_pm": 11.9, "road_pm": 5.4,  "last5": [1,1,0,1,1]},
    "BOS": {"name": "Boston Celtics",         "wins": 43, "losses": 22, "ppg": 119.5, "oppg": 112.4, "home_pm": 10.2, "road_pm": 5.8,  "last5": [0,1,0,1,0]},
    "NYK": {"name": "New York Knicks",        "wins": 42, "losses": 25, "ppg": 114.7, "oppg": 109.8, "home_pm": 8.4,  "road_pm": 2.6,  "last5": [0,1,1,0,1]},
    "LAL": {"name": "Los Angeles Lakers",     "wins": 40, "losses": 25, "ppg": 115.6, "oppg": 111.2, "home_pm": 7.8,  "road_pm": 3.1,  "last5": [1,1,0,1,1]},
    "HOU": {"name": "Houston Rockets",        "wins": 40, "losses": 25, "ppg": 112.9, "oppg": 108.7, "home_pm": 8.9,  "road_pm": 3.4,  "last5": [1,0,1,1,0]},
    "DEN": {"name": "Denver Nuggets",         "wins": 40, "losses": 26, "ppg": 116.3, "oppg": 113.1, "home_pm": 9.6,  "road_pm": 1.8,  "last5": [1,0,1,1,0]},
    "MIN": {"name": "Minnesota Timberwolves", "wins": 40, "losses": 26, "ppg": 113.6, "oppg": 109.4, "home_pm": 8.2,  "road_pm": 2.6,  "last5": [0,1,1,0,0]},
    "CLE": {"name": "Cleveland Cavaliers",    "wins": 40, "losses": 26, "ppg": 113.8, "oppg": 108.4, "home_pm": 9.1,  "road_pm": 3.7,  "last5": [0,1,0,1,0]},
    "PHX": {"name": "Phoenix Suns",           "wins": 38, "losses": 27, "ppg": 114.2, "oppg": 112.0, "home_pm": 6.4,  "road_pm": 0.9,  "last5": [1,1,0,1,0]},
    "MIA": {"name": "Miami Heat",             "wins": 37, "losses": 29, "ppg": 115.1, "oppg": 112.8, "home_pm": 7.2,  "road_pm": 1.4,  "last5": [1,0,1,1,0]},
    "ORL": {"name": "Orlando Magic",          "wins": 36, "losses": 28, "ppg": 110.4, "oppg": 106.9, "home_pm": 7.8,  "road_pm": 1.2,  "last5": [1,0,1,0,1]},
    "TOR": {"name": "Toronto Raptors",        "wins": 36, "losses": 29, "ppg": 112.3, "oppg": 112.1, "home_pm": 4.1,  "road_pm": -0.8, "last5": [0,0,0,1,0]},
    "PHI": {"name": "Philadelphia 76ers",     "wins": 35, "losses": 30, "ppg": 114.6, "oppg": 114.0, "home_pm": 5.2,  "road_pm": -0.4, "last5": [1,0,1,0,0]},
    "ATL": {"name": "Atlanta Hawks",          "wins": 34, "losses": 31, "ppg": 117.2, "oppg": 116.5, "home_pm": 4.8,  "road_pm": -0.2, "last5": [1,0,0,1,1]},
    "CHA": {"name": "Charlotte Hornets",      "wins": 34, "losses": 33, "ppg": 113.5, "oppg": 113.8, "home_pm": 3.8,  "road_pm": -2.1, "last5": [1,0,1,0,1]},
    "LAC": {"name": "LA Clippers",            "wins": 33, "losses": 32, "ppg": 114.8, "oppg": 114.1, "home_pm": 4.4,  "road_pm": -1.6, "last5": [1,0,1,0,1]},
    "GSW": {"name": "Golden State Warriors",  "wins": 32, "losses": 33, "ppg": 113.4, "oppg": 112.9, "home_pm": 5.1,  "road_pm": -2.4, "last5": [0,0,1,1,0]},
    "POR": {"name": "Portland Trail Blazers", "wins": 31, "losses": 35, "ppg": 111.6, "oppg": 114.2, "home_pm": 1.8,  "road_pm": -5.4, "last5": [0,1,0,0,1]},
    "CHI": {"name": "Chicago Bulls",          "wins": 27, "losses": 38, "ppg": 112.1, "oppg": 114.7, "home_pm": 0.6,  "road_pm": -4.8, "last5": [1,0,0,0,1]},
    "MIL": {"name": "Milwaukee Bucks",        "wins": 27, "losses": 37, "ppg": 111.8, "oppg": 114.9, "home_pm": -0.4, "road_pm": -5.2, "last5": [0,1,0,0,0]},
    "MEM": {"name": "Memphis Grizzlies",      "wins": 23, "losses": 41, "ppg": 110.2, "oppg": 116.3, "home_pm": -2.1, "road_pm": -8.4, "last5": [0,0,1,0,0]},
    "NOP": {"name": "New Orleans Pelicans",   "wins": 22, "losses": 45, "ppg": 109.1, "oppg": 116.8, "home_pm": -4.2, "road_pm": -9.8, "last5": [1,0,0,0,0]},
    "DAL": {"name": "Dallas Mavericks",       "wins": 21, "losses": 44, "ppg": 108.8, "oppg": 116.2, "home_pm": -4.8, "road_pm":-10.2, "last5": [1,0,0,0,0]},
    "UTA": {"name": "Utah Jazz",              "wins": 20, "losses": 46, "ppg": 109.7, "oppg": 118.4, "home_pm": -5.4, "road_pm":-12.1, "last5": [1,0,0,0,0]},
    "WAS": {"name": "Washington Wizards",     "wins": 16, "losses": 48, "ppg": 108.9, "oppg": 119.6, "home_pm": -7.1, "road_pm":-13.8, "last5": [0,0,0,0,0]},
    "BKN": {"name": "Brooklyn Nets",          "wins": 17, "losses": 48, "ppg": 108.3, "oppg": 118.7, "home_pm": -6.8, "road_pm":-13.2, "last5": [1,0,0,0,0]},
    "IND": {"name": "Indiana Pacers",         "wins": 15, "losses": 50, "ppg": 108.4, "oppg": 119.3, "home_pm": -7.4, "road_pm":-14.1, "last5": [0,0,0,1,0]},
    "SAC": {"name": "Sacramento Kings",       "wins": 16, "losses": 51, "ppg": 110.1, "oppg": 119.8, "home_pm": -5.8, "road_pm":-13.4, "last5": [1,1,0,0,0]},
}


# ─────────────────────────────────────────────────────────────────────────────
# ALGORITHM
# ─────────────────────────────────────────────────────────────────────────────

def power_rating(team):
    """
    Neutral composite score — no home/away adjustment here.
      win_pct  × 40  → overall record strength
      pt_diff  × 0.8 → scoring dominance per game
      form     × 12  → recent momentum (last 5 games)
    """
    gp       = team["wins"] + team["losses"]
    win_pct  = team["wins"] / gp
    pt_diff  = team["ppg"] - team["oppg"]
    form     = sum(team["last5"]) / len(team["last5"])
    return (win_pct * 40) + (pt_diff * 0.8) + (form * 12)


def road_factor(team):
    """
    How much does this team's performance drop on the road?
    Compares road point margin to overall point diff.
    A factor < 1.0 means they're worse away, > 1.0 means they travel well.
    Clamped to [0.6, 1.3] to avoid extreme outliers.
    """
    overall_diff = team["ppg"] - team["oppg"]
    if abs(overall_diff) < 0.5:
        return 1.0  # roughly neutral team, no meaningful adjustment
    return max(0.6, min(1.3, team["road_pm"] / overall_diff))


def away_adjusted_rating(team):
    """
    Recalculates the away team's power rating with road factor
    applied to the point differential component only.
    Win% and recent form don't change — only the margin component.
    """
    gp      = team["wins"] + team["losses"]
    win_pct = team["wins"] / gp
    pt_diff = team["ppg"] - team["oppg"]
    form    = sum(team["last5"]) / len(team["last5"])
    rf      = road_factor(team)
    return (win_pct * 40) + (pt_diff * rf * 0.8) + (form * 12)


def home_court_advantage(team):
    """
    Team-specific HCA: home point margin minus road point margin.
    This replaces the flat +3.0 used in simpler models.
    e.g. OKC: 14.8 - 9.6 = +5.2 pts at home
    """
    return team["home_pm"] - team["road_pm"]


def calc_spread(home, away):
    """
    Final spread from the home team's perspective.
    Positive = home favored. Negative = away favored.
    Rounded to nearest 0.5 to match sportsbook convention.
    """
    home_rating = power_rating(home)
    away_rating = away_adjusted_rating(away)
    hca         = home_court_advantage(home)
    raw         = home_rating - away_rating + hca
    spread      = round(raw * 2) / 2
    return spread, home_rating, away_rating, hca, raw


def spread_to_moneyline(spread):
    """
    Converts spread to American moneyline odds via logistic sigmoid.
    k = 0.185 is calibrated for NBA (slightly flatter than NFL's 0.22).

    Implied prob:  P = 1 / (1 + e^(-k * spread))
    Favorite ML:   -(p / (1-p)) * 100
    Underdog ML:   +((1-p) / p) * 100
    """
    k          = 0.185
    home_prob  = 1 / (1 + math.exp(-k * spread))
    away_prob  = 1 - home_prob

    def to_american(p):
        if p >= 0.5:
            return -round((p / (1 - p)) * 100)
        return +round(((1 - p) / p) * 100)

    return {
        "home_prob": round(home_prob * 100, 1),
        "away_prob": round(away_prob * 100, 1),
        "home_ml":   to_american(home_prob),
        "away_ml":   to_american(away_prob),
    }


# ─────────────────────────────────────────────────────────────────────────────
# OUTPUT
# ─────────────────────────────────────────────────────────────────────────────

def print_result(home_abbr, away_abbr):
    home = TEAMS[home_abbr]
    away = TEAMS[away_abbr]

    spread, home_rtg, away_rtg, hca, raw = calc_spread(home, away)
    odds = spread_to_moneyline(spread)

    favored = home["name"] if spread >= 0 else away["name"]
    dog     = away["name"] if spread >= 0 else home["name"]

    print("\n" + "─" * 56)
    print(f"  {home['name']} (HOME) vs {away['name']} (AWAY)")
    print("─" * 56)
    print(f"  Spread        : {home_abbr} {spread:+.1f}  ({'home favored' if spread >= 0 else 'away favored'})")
    print(f"  Home ML       : {odds['home_ml']:+d}  ({odds['home_prob']}% implied)")
    print(f"  Away ML       : {odds['away_ml']:+d}  ({odds['away_prob']}% implied)")
    print("─" * 56)
    print(f"  Home rating   : {home_rtg:.2f}  (neutral)")
    print(f"  Away rating   : {away_rtg:.2f}  (road-adjusted)")
    print(f"  Home court adv: +{hca:.1f} pts  ({home_abbr} specific)")
    print(f"  Raw spread    : {raw:.2f}  → rounded to {spread}")
    print(f"  Road factor   : {road_factor(away):.2f}  (1.0 = neutral traveler)")
    print("─" * 56)


def pick_team(prompt, exclude=None):
    """Let the user pick a team by typing abbreviation or part of the name."""
    print(f"\n{prompt}")
    print("Available teams:")
    for abbr, t in sorted(TEAMS.items()):
        marker = "  " if abbr != exclude else "  (already selected)"
        print(f"  {abbr:<4} {t['name']}{marker}")

    while True:
        entry = input("\nEnter abbreviation (e.g. OKC): ").strip().upper()
        if entry in TEAMS and entry != exclude:
            return entry
        if entry == exclude:
            print(f"  That team is already selected as the other side. Pick a different team.")
        else:
            # Try fuzzy match on name
            matches = [k for k, v in TEAMS.items() if entry.lower() in v["name"].lower() and k != exclude]
            if len(matches) == 1:
                return matches[0]
            elif len(matches) > 1:
                print(f"  Multiple matches: {', '.join(matches)}. Be more specific.")
            else:
                print(f"  '{entry}' not found. Try the 3-letter abbreviation.")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("\n========================================")
    print("   NBA SPREAD CALCULATOR  |  2025-26")
    print("========================================")

    while True:
        print("\nOptions:")
        print("  1  Pick your own matchup")
        print("  2  Quick example  (OKC vs BOS)")
        print("  3  Quick example  (SAS vs LAL)")
        print("  q  Quit")

        choice = input("\nChoice: ").strip().lower()

        if choice == "1":
            home_abbr = pick_team("Select the HOME team:")
            away_abbr = pick_team("Select the AWAY team:", exclude=home_abbr)
            print_result(home_abbr, away_abbr)

        elif choice == "2":
            print_result("OKC", "BOS")

        elif choice == "3":
            print_result("SAS", "LAL")

        elif choice == "q":
            print("\nDone.\n")
            break

        else:
            print("  Invalid option.")

        again = input("\nCalculate another matchup? (y/n): ").strip().lower()
        if again != "y":
            print("\nDone.\n")
            break


if __name__ == "__main__":
    main()


import math

def spread_to_implied_probability(spread, k=0.185):
    """
    Stage 3: Spread → Implied Probability
    k = 0.185 for NBA, 0.22 for NFL
    """
    p_home_wins = 1 / (1 + math.exp(-k * spread))
    return p_home_wins

def probability_to_moneyline(p):
    """
    Stage 4: Probability → American Moneyline
    Favorite (p >= 0.50): ML = -(p / (1-p)) * 100
    Underdog (p  < 0.50): ML = +((1-p) / p) * 100
    """
    if p >= 0.50:
        ml = -(p / (1 - p)) * 100   # favorite
    else:
        ml = ((1 - p) / p) * 100    # underdog
    return round(ml)

def calc(spread, k=0.185):
    home_prob = spread_to_implied_probability(spread, k)
    away_prob = 1 - home_prob
    home_ml   = probability_to_moneyline(home_prob)
    away_ml   = probability_to_moneyline(away_prob)

    print(f"\nSpread       : {spread:+.1f}")
    print(f"Home prob    : {home_prob*100:.1f}%  →  ML {home_ml:+d}")
    print(f"Away prob    : {away_prob*100:.1f}%  →  ML {away_ml:+d}")

# ── examples ──────────────────────────────────────────────
calc(-8.5)   # NBA favorite
calc(3.0)    # slight home underdog
calc(-14.0)  # big favorite