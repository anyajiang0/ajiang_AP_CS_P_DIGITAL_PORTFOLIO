"""
THIS IS A SIMULATION, THERE IS *NO* REAL MONEY INVOLVED.
THIS SIMULATION IS NOT INTENDED TO ENCOURAGE GAMBLING IN ANY WAY, SHAPE, OR FORM.
"""
# imports 

import http.server
import json
import urllib.parse 

# settings


# spread calc (bear with me here)
home_court_advantage = 3.0
# home_rating and away_rating are calculated using data from an API 
spread = home_rating - away_rating + home_court_advantage 