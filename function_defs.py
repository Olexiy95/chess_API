import requests
import json

"""
Function definitions for different available endpoins.
"""

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
    endpointUrl = "player/{}".format(username)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()

def get_stats(username):
    endpointUrl = "player/{}/stats".format(username)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()


def get_titled_players(title):
    """
    Valid title abbreviations are: 
    GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM.
    """
    endpointUrl = "titled/{}".format(title)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()


def get_online_status(username):
    endpointUrl = "player/{}/is-online".format(username)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()

def get_daily_games(username, to_move_flag):
    if to_move_flag == False:
        endpointUrl = "player/{}/games".format(username)
    elif to_move_flag == True:
        endpointUrl = "player/{}/games/to-move".format(username)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()

def get_game_archives(username):
    endpointUrl = "player/{}/games/archives".format(username)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()

def get_finished_games(username, MM, YYYY):
    endpointUrl = "player/{}/games/{}/{}".format(username, YYYY, MM)
    requestUrl = baseUrl + endpointUrl
    request = requests.get(requestUrl)
    return request.json()

def get_finished_games_pgn(username, MM, YYYY):
    endpointUrl = "player/{username}/games/{YYYY}/{MM}/pgn".format(username,YYYY, MM)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.content()

def get_player_clubs(username):
    endpointUrl = "player/{}/clubs".format(username)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_team_matches(username):
    endpointUrl = "player/{}/matches".format(username)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_tournaments(username):
    endpointUrl = "player/{}/tournaments".format(username)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_club(club_url):
    endpointUrl = "club/{}".format(club_url)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_club_members(club_url):
    endpointUrl = "club/{}/members".format(club_url)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_club_matches(club_url):
    endpointUrl = "club/{}/matches".format(club_url)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_tournament(tournament_url):
    endpointUrl = "tournament/{}".format(tournament_url)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_tournament_round(tournament_url, round):
    endpointUrl = "tournament/{}/{}".format(tournament_url, round)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_tournament_round_group(tournament_url, round, group):
    endpointUrl = "tournament/{}/{}/{}".format(tournament_url, round, group)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_match(match_id):
    endpointUrl = "match/{}".format(match_id)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_match_board(match_id, board):
    endpointUrl = "match/{}/{}".format(match_id, board)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_live_match(live_id):
    endpointUrl = "match/live/{}".format(live_id)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_live_match_board(live_id, board):
    endpointUrl = "match/live/{}/{}".format(live_id, board)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_country(country_iso):
    # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    endpointUrl = "country/{}".format(country_iso)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_country_players(country_iso):
    # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    endpointUrl = "country/{}/players".format(country_iso)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_country_clubs(country_iso):
    # https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
    endpointUrl = "country/{}/clubs".format(country_iso)
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_puzzle():
    endpointUrl = "puzzle"
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_random_puzzle():
    endpointUrl = "puzzle/random"
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_streamers():
    endpointUrl = "streamers"
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()

def get_leadeboards():
    endpointUrl = "leaderboards"
    requestUrl = baseUrl + endpointUrl
    request = request.get(requestUrl)
    return request.json()