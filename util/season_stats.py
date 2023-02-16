import asyncio
import pandas as pd

def get_stats_for_team(team_site: str, sport: str):
    url = f"https://{team_site}.com/sports/{sport}/stats/2022-23"
    tables = pd.read_html(url, header=1)
    df: pd.DataFrame = tables[4]
    df.drop(df.tail(2).index, inplace = True)
    df["Player"] = df["Player"].str.split("  ").str[0]
    df["FG%"] = df["FG%"].apply(lambda x: "{:.1%}".format(x))
    df["3PT%"] = df["3PT%"].apply(lambda x: "{:.1%}".format(x))
    df["FT%"] = df["FT%"].apply(lambda x: "{:.1%}".format(x))
    df.rename({"PTS": "PPG", "REB": "RPG", "AST": "APG", "STL": "SPG"}, inplace=True)
    return df.to_dict(orient="records")


async def run(queue: asyncio.Queue, params: dict):
    loop = asyncio.get_event_loop()
    home_team = params.get("homeTeam")
    away_team = params.get("awayTeam")
    home_stats = await loop.run_in_executor(None, get_stats_for_team, home_team)
    away_stats = await loop.run_in_executor(None, get_stats_for_team, away_team)
    payload = {
        "homeSeasonStats": home_stats,
        "awaySeasonStats": away_stats
    }
    await queue.put({"sender": "Season Stats", "payload": payload})


if __name__ == "__main__":
    get_stats_for_team("drexeldragons", "womens-basketball")