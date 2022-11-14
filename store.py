""" key-value store attached to queue """

import asyncio

from loguru import logger

from app import sio
from plugins.livestats import run_home_player_update

STORE = {"foo": "bar", "bugFlying": False}

STORE_LISTENERS = {
    "homePlayerNum": run_home_player_update
}


async def store_patch(payload: dict):
    STORE.update(payload)
    await sio.emit("store_patch", payload)


async def queue_watcher(queue: asyncio.Queue):
    while True:
        message: dict = await queue.get()
        payload: dict = message.get("payload", {})
        sender: str = message.get("sender", "")

        await store_patch(payload)
        # logger.debug(f"Plugin {sender} send patch: {payload}")


@sio.event
async def connect(sid, _):
    logger.info(f"Client {sid} connected.")
    await sio.emit("store_init", STORE, sid)


@sio.event
async def store_update(sid, payload: dict):
    await store_patch(payload)
    listener = STORE_LISTENERS.get(payload)
    if listener:
        await listener()
    logger.debug(f"Client {sid} sent patch: {payload}")
