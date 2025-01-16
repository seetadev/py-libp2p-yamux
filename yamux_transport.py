from yamux import YamuxTransport
from libp2p.transport.tcp.tcp import TCP

class YamuxTransportWrapper:
    def __init__(self):
        self.base_transport = TCP()
        self.yamux_transport = YamuxTransport(self.base_transport)

    async def dial(self, peer_id, endpoint):
        return await self.yamux_transport.dial(peer_id, endpoint)

    async def listen(self, endpoint):
        return await self.yamux_transport.listen(endpoint)
