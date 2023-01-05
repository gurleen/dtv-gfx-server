"""Plugin for After Effects render automation"""
import asyncio
import shlex

from loguru import logger

from app import sio, queue
from util.db import delete_row_with_id, get_all_from_db, insert_into_db


DATABASE_NAME = "aerender_db.json"
AERENDER_TIMEOUT = 10
AERENDER_COMMAND = """
/Applications/Adobe\ After\ Effects\ 2022/aerender 
-project {project}
-comp "{comp}"
-s {start_frame}
-e {end_frame} 
-output /Users/gurleen/Desktop/{output}.mov
-RStemplate "Best Settings" 
-OMtemplate "DTV Output"
"""


def get_render_command(
    project: str, comp: str, start_frame: int, end_frame: int, output: str, **kwargs
) -> str:
    return AERENDER_COMMAND.format(
        project=project,
        comp=comp,
        start_frame=start_frame,
        end_frame=end_frame,
        output=output,
    )


async def execute_aerender(command: str, frames: int, id: int):
    args = shlex.split(command)
    print(args)
    proc = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE)

    try:
        while proc.returncode is None:
            line = await asyncio.wait_for(proc.stdout.readline(), AERENDER_TIMEOUT)
            try:
                line = line.decode("ascii")
                p_open, p_close = line.index("("), line.index(")")
                frame = int(line[p_open + 1 : p_close])
                progress = frame / frames
                await queue.put(
                    {
                        "payload": {f"render_job_{id}_progress": progress},
                        "sender": "AERender",
                    }
                )
            except:
                progress = 0
    except asyncio.TimeoutError:
        logger.error("aerender timed out!")

    await queue.put({"payload": {"aerender_progress": 0}, "sender": "AERender"})
    logger.info("Render finished!")


@sio.event
async def run_render(_, data: dict):
    command = get_render_command(**data)
    await execute_aerender(command, data["end_frame"], data["id"])
    return "ok"


@sio.event
async def store_preset(_, data: dict):
    keys = ["output", "project", "comp", "start_frame", "end_frame"]
    is_valid = all(key for key in keys if key in data)
    if is_valid:
        filtered_data = {k: data[k] for k in data if k in keys}
        await insert_into_db(DATABASE_NAME, filtered_data)


@sio.event
async def get_presets(_):
    return await get_all_from_db(DATABASE_NAME)


@sio.event
async def remove_preset(_, id: int):
    return await delete_row_with_id(DATABASE_NAME, id)


logger.info("Initialized AE Renderer.")
