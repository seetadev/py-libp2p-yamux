import asyncio
from typing import Optional

class YamuxStream:
    def __init__(self, stream_id: int, transport: 'YamuxTransport'):
        self.stream_id = stream_id
        self.transport = transport
        self.read_queue = asyncio.Queue()
        self.write_queue = asyncio.Queue()
        self.closed = False

    async def read(self) -> Optional[bytes]:
        if self.closed:
            return None
        return await self.read_queue.get()

    async def write(self, data: bytes):
        if self.closed:
            raise Exception("Stream is closed")
        await self.write_queue.put(data)

    async def close(self):
        self.closed = True
        await self.transport.close_stream(self.stream_id)

class YamuxTransport:
    def __init__(self, base_transport):
        self.base_transport = base_transport
        self.streams = {}
        self.next_stream_id = 1
        self.lock = asyncio.Lock()

    async def dial(self, peer_id, endpoint):
        connection = await self.base_transport.dial(peer_id, endpoint)
        return YamuxStream(self._get_next_stream_id(), self)

    async def listen(self, endpoint):
        listener = await self.base_transport.listen(endpoint)
        return YamuxStream(self._get_next_stream_id(), self)

    async def close_stream(self, stream_id: int):
        if stream_id in self.streams:
            del self.streams[stream_id]

    def _get_next_stream_id(self) -> int:
        with self.lock:
            stream_id = self.next_stream_id
            self.next_stream_id += 1
        return stream_id
