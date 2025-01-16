import asyncio
import unittest
from yamux import YamuxStream, YamuxTransport

class TestYamux(unittest.TestCase):
    def setUp(self):
        self.transport = YamuxTransport(None)

    async def test_stream_read_write(self):
        stream = YamuxStream(1, self.transport)
        await stream.write(b"Hello")
        data = await stream.read()
        self.assertEqual(data, b"Hello")

    async def test_stream_close(self):
        stream = YamuxStream(1, self.transport)
        await stream.close()
        with self.assertRaises(Exception):
            await stream.write(b"Data after close")

if __name__ == "__main__":
    unittest.main()
