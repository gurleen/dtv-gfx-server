import asyncio
from importlib import import_module
from typing import Coroutine, Optional
from loguru import logger
from first import first

from app import sio


task_list = []


def resolve_coro(coro_name: str) -> Optional[Coroutine]:
    pkg, name = coro_name.rsplit(".", 1)
    try:
        mod = import_module(pkg)
    except Exception as e:
        logger.error(e)
        return
    coro = getattr(mod, name, None)
    return coro


def init_tasks(tasks: list[dict], queue: asyncio.Queue):
    global task_list
    task_list = tasks
    loop = asyncio.get_event_loop()
    task_objects = set()
    for task in tasks:
        name = task.get("name")
        coroutine_name = task.get("coroutine")
        is_import_only = task.get("importOnly")

        if is_import_only:
            try:
                import_module(coroutine_name)
            finally:
                continue

        logger.info(f"Initializing plugin {name} from {coroutine_name}...")
        params = task.get("params", {})

        coro = resolve_coro(coroutine_name)
        if coro:
            task_obj = loop.create_task(coro(queue, params), name=name)
            task_objects.add(task_obj)

    return task_objects


def get_tasks_status() -> dict[str, bool]:
    tasks = asyncio.all_tasks()
    running = [
        {"name": task.get_name(), "running": not (task.cancelled() or task.done())}
        for task in tasks
        if not task.get_name().startswith("Task")
    ]
    running_task_names = [t["name"] for t in running]
    print(running_task_names)
    stopped = [
        {"name": task["name"], "running": False}
        for task in task_list
        if task["name"] not in running_task_names
        and not task["importOnly"]
    ]
    return [*running, *stopped]


@sio.event
async def task_status(_):
    return get_tasks_status()


@sio.event
async def cancel_task(_, name: str):
    all_tasks = asyncio.all_tasks()
    task = first(all_tasks, key=lambda t: t.get_name() == name)
    print(task)
    if task:
        task.cancel()
    await task
    print(f"Cancelling {task.get_name()}")