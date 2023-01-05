import asyncio
from util.ncaa import get_ncaa_json, filter_games_by_conf, normalize_game_data


async def run(queue: asyncio.Queue, params: dict):
    while True:
        ncaa_json = get_ncaa_json(sport=params.get("sport", "basketball-women"))
        caa_games = filter_games_by_conf(ncaa_json, "CAA")
        caa_norm = [normalize_game_data(g) for g in caa_games]
        await queue.put({"sender": "CAA Out of Town Scores", "payload": {"caa_games": caa_norm}})
        await asyncio.sleep(120)