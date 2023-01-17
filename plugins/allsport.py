"""Plugin for AllSport CG Serial feed"""

import asyncio
import random
import traceback
import serial_asyncio
from loguru import logger
import aiofiles

from itertools import cycle
from datetime import timedelta

from store import STORE, store_patch


ALLSPORT_LINE_MAPS = {
    "soccer": {
        "clock": (0, 5),
        "home_score": (25, 27),
        "away_score": (27, 29)
    },
    "basketball": {
        "clock": (0, 5),
        "homeScore": (13, 15),
        "awayScore": (15, 18),
        "shotClock": (8, 10),
    },
    "clock_only": {
        "clock": (0, 5)
    },
}

LIVETEXT_FILE = "livetext.txt"


def print_debug_numbers(line: str):
    cyc = cycle(range(10))
    for _ in line:
        print(next(cyc), end="")
    print()


def parse_line_for_sport(line: str, sport: str) -> dict[str, str]:
    sport_map = ALLSPORT_LINE_MAPS.get(sport, {})
    parsed_values = dict()
    for key, range in sport_map.items():
        start, end = range
        parsed_values[key] = line[start:end].strip()
    return parsed_values


def time_to_secs(time: str) -> timedelta:
    minutes, seconds = time.split(":")
    return 60 * int(minutes) + int(seconds)


def seconds_to_time_str(seconds: int) -> str:
    m, s = divmod(seconds, 60)
    return f"{m}:{s:02d}"


async def update_droughts(parsed_values: dict):
    clock = parsed_values["clock"]
    for side in ["home", "away"]:
        selected_trend = STORE.get(f"{side}Trend")
        prefix = "NO FGs LAST" if "FG" in selected_trend else "SCORING DROUGHT"
        value = STORE.get(selected_trend)
        new_value = seconds_to_time_str(time_to_secs(value) - time_to_secs(clock))
        await store_patch({f"{side}TrendText": f"{prefix} {new_value}"})


def package_payload(parsed_values: dict) -> dict:
    return {"payload": parsed_values, "sender": "AllSport CG Plugin"}


async def write_to_livetext(parsed_values: dict):
    async with aiofiles.open(LIVETEXT_FILE, "w") as f:
        for k, v in parsed_values.items():
            await f.write(f"{k}={v}")


async def read_allsport_cg(queue: asyncio.Queue, params: dict):
    logger.info("Running AllSport CG Reader.")
    port = params.get("port", "COM3")
    sport = params.get("sport", "basketball")
    LIVETEXT_FILE = params.get("livetext_file", "livetext.txt")
    reader, _ = await serial_asyncio.open_serial_connection(url=port)
    try:
        while True:
            line = await reader.readuntil(separator=b"\x04")
            decoded_line = line.decode("ascii").lstrip("\x01")
            parsed_values = parse_line_for_sport(decoded_line, sport)
            payload = package_payload(parsed_values)
            await write_to_livetext(parsed_values)
            try:
                await update_droughts(parsed_values)
            except Exception:
                logger.error("Failed to update scoring droughts.")
            await queue.put(payload)
    except asyncio.CancelledError as e:
        traceback.print_exc()
        logger.info("Serial connection closed.")


async def mock_allsport_cg(queue: asyncio.Queue, params: dict):
    clock = 600
    home_score, away_score = 0, 0
    while True:
        m, s = divmod(clock, 60)
        clock_str = f"{m}:{s:02d}"
        await queue.put({"sender": "Mock AllSport CG", "payload": {"clock": clock_str}})
        await update_droughts({"clock": clock_str})
        clock -= 1
        if clock <= 0:
            clock = 600
        """
        if random.random() > 0.90:
            home_score += random.choice((2, 3))
            await queue.put(
                {"sender": "Mock AllSport CG", "payload": {"homeScore": home_score}}
            )
        if random.random() > 0.90:
            away_score += random.choice((2, 3))
            await queue.put(
                {"sender": "Mock AllSport CG", "payload": {"awayScore": away_score}}
            )
        """
        await asyncio.sleep(1)
