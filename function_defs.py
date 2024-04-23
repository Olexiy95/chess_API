import requests
import json

"""
Function definitions for different available endpoins.
"""


class ChessAPI:
    def __init__(self):
        self.base_url = "https://api.chess.com/pub/"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def get_profile(self, username):
        return self.get(f"player/{username}")

    def get_stats(self, username):
        return self.get(f"player/{username}/stats")

    def get_titled_players(self, title):
        """
        Valid title abbreviations are:
        GM, WGM, IM, WIM, FM, WFM, NM, WNM, CM, WCM.
        """
        return self.get(f"titled/{title}")

    def get_online_status(self, username):
        return self.get(f"player/{username}/is-online")

    def get_daily_games(self, username, to_move_flag: bool = False):
        if to_move_flag == False:
            return self.get(f"player/{username}/games")
        elif to_move_flag == True:
            return self.get(f"player/{username}/games/to-move")

    def get_game_archives(self, username):
        return self.get(f"player/{username}/games/archives")

    def get_finished_games(self, username, MM, YYYY):
        return self.get(f"player/{username}/games/{YYYY}/{MM}")

    def get_finished_games_pgn(self, username, MM, YYYY):
        return self.get(f"player/{username}/games/{YYYY}/{MM}/pgn")

    def get_player_clubs(self, username):
        return self.get(f"player/{username}/clubs")

    def get_team_matches(self, username):
        return self.get(f"player/{username}/matches")

    def get_tournaments(self, username):
        return self.get(f"player/{username}/tournaments")

    def get_club(self, club_url):
        return self.get(f"club/{club_url}")

    def get_club_members(self, club_url):
        return self.get(f"club/{club_url}/members")

    def get_club_matches(self, club_url):
        return self.get(f"club/{club_url}/matches")

    def get_tournament(self, tournament_url):
        return self.get(f"tournament/{tournament_url}")

    def get_tournament_round(self, tournament_url, round):
        return self.get(f"tournament/{tournament_url}/{round}")

    def get_tournament_round_group(self, tournament_url, round, group):
        return self.get(f"tournament/{tournament_url}/{round}/{group}")

    def get_match(self, match_id):
        return self.get(f"match/{match_id}")

    def get_match_board(self, match_id, board):
        return self.get(f"match/{match_id}/{board}")

    def get_live_match(self, live_id):
        return self.get(f"match/live/{live_id}")

    def get_live_match_board(self, live_id, board):
        return self.get(f"match/live/{live_id}/{board}")

    def get_country(self, country_iso):
        """https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"""
        return self.get(f"country/{country_iso}")

    def get_country_players(self, country_iso):
        """https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"""
        return self.get(f"country/{country_iso}/players")

    def get_country_clubs(self, country_iso):
        """https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"""
        return self.get(f"country/{country_iso}/clubs")

    def get_puzzle(self):
        return self.get("puzzle")

    def get_random_puzzle(self):
        return self.get("puzzle/random")

    def get_streamers(self):
        return self.get("streamers")

    def get_leadeboards(self):
        return self.get("leaderboards")

    def get(self, endpoint: str):
        response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        if response.status_code not in (200, 201):
            print(response.text)
        response.raise_for_status()
        return response.json()
