import asyncio
import json

from aiohttp import web
import socketio


def read_config() -> dict:
    with open("./config.json", mode="r") as conf:
        contents = conf.read()
        return json.loads(contents)


async def on_response_prepare(_: web.Request, response: web.Response):
    response.headers["Cache-control"] = "no-cache"


sio = socketio.AsyncServer(async_mode="aiohttp", cors_allowed_origins="*")
app = web.Application()
sio.attach(app)

queue = asyncio.Queue()

app.router.add_static("/", "./dashboard", show_index=True)
# app.router.add_static("/gfx", "./static", show_index=True)

app.on_response_prepare.append(on_response_prepare)


def setup_web_runner(loop):
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner)
    loop.run_until_complete(site.start())
