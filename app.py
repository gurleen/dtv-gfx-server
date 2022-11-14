import json

from aiohttp import web
import socketio
from janus import Queue


def read_config() -> dict:
    with open("./config.json", mode="r") as conf:
        contents = conf.read()
        return json.loads(contents)


sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

full_queue = Queue()
queue = full_queue.async_q
sync_queue = full_queue.sync_q

app.router.add_static("/", "./dashboard", show_index=True)
# app.router.add_static("/gfx", "./static", show_index=True)

def setup_web_runner(loop):
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner)
    loop.run_until_complete(site.start())