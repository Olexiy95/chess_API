import requests
import json

# Define Functions Here

baseUrl = "https://api.chess.com/pub/"

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def template(parameter):
    endpointUrl = ""
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_profile(username):
    requestUrl = baseUrl + username
    request = requests.get(requestUrl)
    return request.json()

def get_stats(username):
    baseUrl = "https://api.chess.com/pub/player/"
    requestUrl = baseUrl + username + "/stats"
    request = requests.get(requestUrl)
    return request.json()


def get_titled_players(title):
    """
    Valid title abbreviations are: 
    GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM.
    """
    baseUrl = "https://api.chess.com/pub/titled/"
    requestUrl = baseUrl + title
    request = requests.get(requestUrl)
    return request.json()


def get_online_status(username):
    baseUrl = "https://api.chess.com/pub/player/"
    requestUrl = baseUrl + username + "/is-online"
    request = requests.get(requestUrl)
    return request.json()

def get_daily_games(username):
    baseUrl = "https://api.chess.com/pub/player/"
    requestUrl = baseUrl + username + "/games"
    request = requests.get(requestUrl)
    return request.json()

def get_games_to_move(username):
    baseUrl = "https://api.chess.com/pub/player/"
    requestUrl = baseUrl + username + "/games/to-move"
    request = requests.get(requestUrl)
    return request.json()

def get_game_archives(username):
    baseUrl = "https://api.chess.com/pub/player/"
    requestUrl = baseUrl + username + "/games/archives"
    request = requests.get(requestUrl)
    return request.json()

def get_game_archives(username):
    baseUrl = "https://api.chess.com/pub/player/"
    requestUrl = baseUrl + username + "/games/archives"
    request = requests.get(requestUrl)
    return request.json()

def get_finished_games(username, MM, YYYY):
    baseUrl = "https://api.chess.com/pub/player/"
    endpointUrl = 
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()

# https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}

#  https://api.chess.com/pub/player/{username}/games/{YYYY}/{MM}/pgn

#  https://api.chess.com/pub/player/{username}/clubs

#  https://api.chess.com/pub/player/{username}/matches

#  https://api.chess.com/pub/player/{username}/tournaments

#  https://api.chess.com/pub/club/{url-ID}

#  https://api.chess.com/pub/club/{url-ID}/members

# https://api.chess.com/pub/club/{ID}/matches

# https://api.chess.com/pub/tournament/{url-ID}

# https://api.chess.com/pub/tournament/{url-ID}/{round}

# https://api.chess.com/pub/tournament/{url-ID}/{round}/{group}

# https://api.chess.com/pub/match/{ID}

#  https://api.chess.com/pub/match/{ID}/{board}

#   https://api.chess.com/pub/match/live{ID}

#   https://api.chess.com/pub/match/live/{ID}/{board}

#   https://api.chess.com/pub/country/{iso}

#   https://api.chess.com/pub/country/{iso}/players

#   https://api.chess.com/pub/country/{iso}/clubs

#   https://api.chess.com/pub/puzzle

#   https://api.chess.com/pub/puzzle/random

#    https://api.chess.com/pub/streamers

#    https://api.chess.com/pub/leaderboards