#!/home/kafonek/maelstrom_python/.venv/bin/python
import asyncio

from lib.models import Broadcast, BroadcastOk, Read, ReadOk, Topology, TopologyOk
from lib.server import Server


class BroadcastServer(Server):
    def __init__(self):
        super().__init__()
        self.messages_seen = set()

    async def handle_topology(self, src: str, body: Topology):
        reply = TopologyOk(in_reply_to=body.msg_id, msg_id=self.get_msg_id())
        await self.send(dest=src, body=reply)

    async def handle_broadcast(self, src: str, body: Broadcast):
        self.messages_seen.add(body.message)
        reply = BroadcastOk(in_reply_to=body.msg_id, msg_id=self.get_msg_id())
        await self.send(dest=src, body=reply)

    async def handle_read(self, src: str, body: Read):
        reply = ReadOk(
            in_reply_to=body.msg_id, msg_id=self.get_msg_id(), messages=list(self.messages_seen)
        )
        await self.send(dest=src, body=reply)


if __name__ == "__main__":
    server = BroadcastServer()
    asyncio.run(server.run())
