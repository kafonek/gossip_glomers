#!/home/kafonek/maelstrom_python/.venv/bin/python
import asyncio

from lib.models import Echo, EchoOk
from lib.server import Server


class EchoServer(Server):
    async def handle_echo(self, src: str, body: Echo):
        reply = EchoOk(in_reply_to=body.msg_id, msg_id=self.get_msg_id(), echo=body.echo)
        await self.send(dest=src, body=reply)


if __name__ == "__main__":
    server = EchoServer()
    asyncio.run(server.run(), debug=True)
