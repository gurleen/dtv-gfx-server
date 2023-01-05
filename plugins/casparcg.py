import asyncio
from amcp_pylib.core import ClientAsync
from amcp_pylib.module.query import INFO


HOST_NAME = "localhost"
PORT = 6969


client = ClientAsync()
asyncio.get_running_loop().run_until_complete(client.connect(HOST_NAME, PORT))


class CasparCGClient:
    async def get_videos(self):
        res = await client.send(INFO())
        print(res)
