import asyncio
import json
import shlex

from app import sio, queue
from util.db import delete_row_with_id, get_all_from_db, insert_into_db


NEXRENDER_DB = "nexrender_db.json"


async def run_render(preset: dict):
    template_str = json.dumps(preset)
    command = f"nexrender-cli '{template_str}'"
    args = shlex.split(command)

    proc = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE)
    code = await proc.wait()
    print(f"nexrender exited with code {code}")


@sio.event
async def nexrender_run_render(_, preset: dict):
    await run_render(preset)


@sio.event
async def nexrender_get_all_presets(_):
    return await get_all_from_db(NEXRENDER_DB)


@sio.event
async def nexrender_store_preset(_, preset: dict):
    return await insert_into_db(NEXRENDER_DB, preset)


@sio.event
async def nexrender_remove_preset(_, id: int):
    return await delete_row_with_id(NEXRENDER_DB, id)
