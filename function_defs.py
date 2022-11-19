import requests
import json

# Define Functions Here

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def get_profile(username):
    baseUrl = "https://api.chess.com/pub/player/"
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

