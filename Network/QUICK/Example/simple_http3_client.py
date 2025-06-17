import asyncio
from aioquic.asyncio import connect
from aioquic.asyncio import QuicConnection
from aioquic.quic.configuration import QuicConfiguration
from aioquic.quic.events import HandshakeCompleted
from aioquic.quic.events import HandshakeFailed
from aioquic.quic.events import DataReceived

# this is async fetch, hight efficiency
async def fetch():
    configuration = QuicConfiguration(is_client=True)
    async with connect('example.com', 4433, configuration=configuration) as protocol:
        # 发送 GET 请求
        protocol.transmit(b'GET / HTTP/3\r\n\r\n')
        # 等待响应
        while True:
            event = await protocol.receive()
            if isinstance(event, HandshakeCompleted):
                print("Handshake completed")
            elif isinstance(event, DataReceived):
                print("Received data:", event.data)
                break
            elif isinstance(event, HandshakeFailed):
                print("Handshake failed")
                break

asyncio.run(fetch())


# this is the sync fetch not async fetch. low efficient
import http3
def fetch():
    client = http3.Client()
    response = client.get('https://example.com')
    print(response.status_code)
    print(response.text)