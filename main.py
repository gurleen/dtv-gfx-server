import asyncio

from loguru import logger

from app import read_config, setup_web_runner, queue
from tasks import init_tasks
from store import queue_watcher


def main():
    loop = asyncio.get_event_loop()
    setup_web_runner(loop)

    loop.create_task(queue_watcher(queue))

    config = read_config()
    _ = init_tasks(config["plugins"], queue)

    logger.info("Running DragonsTV Graphics Server")

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.stop()
        logger.info("Exiting DragonsTV Graphics Server.")
        exit()


if __name__ == "__main__":
    main()
