import asyncio
import json

from app import sio, queue
from store import STORE
from loguru import logger
from .stat_names import STAT_NAMES
from ncaa_live_stats import NCAALiveStats, Game
from ncaa_live_stats.compose.player import compose_player_statline

PARAMS = {
    "type": "parameters",
    "types": "se,ac,mi,te,sc,pbp,box",
    "playbyplayOnConnect": 1,
}

FORMATTED_PARAMS = json.dumps(PARAMS).encode()


stats = NCAALiveStats()


async def read_live_stats(queue: asyncio.Queue, params: dict):
    LISTENERS = {
        "boxscore": [update_home_player, update_away_player, update_comp_stat]
    }

    logger.info("Running NCAA Live Stats listener")

    reader, writer = await asyncio.open_connection("10.250.37.65", 7677)

    writer.write(FORMATTED_PARAMS)
    await writer.drain()

    while True:
        line = await reader.readuntil(b"\r\n")
        decoded_line = line.decode()
        payload = json.loads(decoded_line)
        p_type = payload.get("type", "")
        stats.receive(payload)
        if p_type in LISTENERS:
            funcs = LISTENERS[p_type]
            for f in funcs:
                try:
                    await f(stats._game)
                finally:
                    continue


def get_starters(game: Game):
    home_starters = [
        p.full_name for p in game.home_team.players.values() if p.is_starter
    ]
    logger.info(f"Home starters: {home_starters}")
    away_starters = [
        p.full_name for p in game.away_team.players.values() if p.is_starter
    ]
    logger.info(f"Away starters: {away_starters}")

    has_all_starters = len(home_starters) == 5 and len(away_starters) == 5
    if has_all_starters:
        logger.info("All starters located.")


stats.add_listener("teams", get_starters)


async def update_home_player(game: Game):
    current_player_num = STORE.get("homePlayerNum")
    player = game.home_team.get_player_by_shirt(current_player_num)
    line = compose_player_statline(player)

    payload = {
        "homePlayerName": player.full_name.upper(),
        "homePlayerPos": player.position,
        "homePlayerShirt": player.shirt,
        "homePlayerLine": line
    }

    await queue.put({"sender": "NCAA Live Stats", "payload": payload})


async def update_away_player(game: Game):
    current_player_num = STORE.get("awayPlayerNum")
    player = game.away_team.get_player_by_shirt(current_player_num)
    line = compose_player_statline(player)

    payload = {
        "awayPlayerName": player.full_name.upper(),
        "awayPlayerPos": player.position,
        "awayPlayerShirt": player.shirt,
        "awayPlayerLine": line
    }

    await queue.put({"sender": "NCAA Live Stats", "payload": payload})


async def update_comp_stat(game: Game):
    stat = STORE.get("compStat", "assists")
    home_stat = getattr(game.home_team.game_stats, stat)
    away_stat = getattr(game.away_team.game_stats, stat)
    if home_stat and away_stat:
        payload = {
            "compStatTitle": STAT_NAMES.get(stat, ""),
            "compStatLine": f"DREXEL: {home_stat}     PENN: {away_stat}"
        }

        await queue.put({"sender": "NCAA Live Stats", "payload": payload})

@sio.event
async def run_home_update(_):
    await update_home_player(stats._game)


@sio.event
async def run_away_update(_):
    await update_away_player(stats._game)


@sio.event
async def run_comp_update(_):
    await update_comp_stat(stats._game)


@sio.event
async def export_stat_line():
    global stats
    line = str()
    top_five_home = sorted(stats._game.home_team.players.values(), key=lambda p: p.stats.points, reverse=True)[:5]
    top_five_away = sorted(stats._game.away_team.players.values(), key=lambda p: p.stats.points, reverse=True)[:5] 
    for player in [*top_five_home, *top_five_away]:
        stats = player.stats
        p_line = f"#{player.shirt} {player.last_name.capitalize()}: {stats.points} PTS, {stats.assists} AST, {stats.rebounds_total} REB"
        line += p_line + " --- "
    
    return line