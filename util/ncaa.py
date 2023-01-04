from datetime import datetime
import requests
from pprint import pprint


LOGO_URL_FORMAT = "https://i.turner.ncaa.com/sites/default/files/images/logos/schools/bgl/{school}.svg"


def normalize_game_data(game: dict) -> dict:
    return {
        "homeName": game["home"]["names"]["char6"],
        "awayName": game["away"]["names"]["char6"],
        "homeScore": game["home"]["score"],
        "awayScore": game["away"]["score"],
        "startTime": game["startTime"],
        "period": game["currentPeriod"],
        "homeLogo": LOGO_URL_FORMAT.format(school=game["home"]["names"]["seo"]),
        "awayLogo": LOGO_URL_FORMAT.format(school=game["away"]["names"]["seo"])
    }


def filter_games_by_conf(ncaa_json: dict, conf: str) -> list[dict]:
    return [
        g["game"]
        for g in ncaa_json["games"]
        if g["game"]["home"]["conferences"][0]["conferenceName"] == conf
    ]


def get_ncaa_json(sport: str = "basketball-men") -> dict:
    today = datetime.today()
    url = f"https://data.ncaa.com/casablanca/scoreboard/{sport}/d1/{today.year}/{today.month:02d}/{today.day:02d}/scoreboard.json"
    url = f"https://data.ncaa.com/casablanca/scoreboard/{sport}/d1/2023/01/01/scoreboard.json"
    req = requests.get(url)
    return req.json()


def main():
    json = get_ncaa_json(sport="basketball-women")
    caa = filter_games_by_conf(json, "CAA")
    caa_norm = [normalize_game_data(g) for g in caa]
    pprint(caa_norm)


if __name__ == "__main__":
    main()
