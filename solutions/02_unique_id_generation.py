#!/home/kafonek/maelstrom_python/.venv/bin/python
import asyncio
import uuid

from lib.models import Generate, GenerateOk
from lib.server import Server


class GenerateServer(Server):
    async def handle_generate(self, src: str, body: Generate):
        reply = GenerateOk(in_reply_to=body.msg_id, msg_id=self.get_msg_id(), id=uuid.uuid4().int)
        await self.send(dest=src, body=reply)


if __name__ == "__main__":
    server = GenerateServer()
    asyncio.run(server.run(), debug=True)
