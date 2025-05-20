# WebSocket 基本原理

With one Statement: WebSocket is after web-client send a HTTP request to server, it will get the response which include all the basic info about TCP establishment. After that, Client will connection to the server, and keep the connection till the end of Application.

## Connection

WebSocket Connection start from Client's HTTP request:

```HTTP
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec=WebSocket-Key: XXXXXXX
Sec-WebSocket-Version: 13
```

Server will feedback the response with 101 state while received the request:

```HTTP
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-Websocket-accept: XXXXXX
```

after hand-shake, they build the persistent and full-duplex TCP connection.
all the tcp connection build are all be implement at the underlying logic (底层逻辑)

## Data Transfer (Communication period)

After the connection built, receive and send data each other. WebSocket only support text and binary frame. Allow the Text with UTF-8 formant and binary data. in the process, server can push data to client with out client request.

## Connection Closing (Break Connection)

Any of two side can brake can close connection with OpCode 0x8. Close Frame can include a status code and option close reason. Send another close frame when other side need send another close frame.

## Frame Format

```lua
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-------+-+-------------+-----------------------+
|F|R|R|R| opcode|M| Payload len |    Extended payload length    |
|I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
|N|V|V|V|       |S|             |   (if payload len==126/127)   |
+-+-+-+-+-+-+-+-+-------+-+-------------+ - - - - - - - - - - - +
|     Extended payload length continued, if payload len == 127  |
+ - - - - - - - - - - - - - - - +-------------------------------+
|                               |Masking-key, if MASK set to 1  |
+-------------------------------+-------------------------------+
| Masking-key (continued)       |          Payload Data         |
+-------------------------------- - - - - - - - - - - - - - - - +
:                     Payload Data continued ...                :
+ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
|                     Payload Data continued ...                |
+---------------------------------------------------------------+

```

各字段含义如下：
FIN（1 位）：

    表示是否为消息的最后一帧。1 表示是最后一帧，0 表示后续还有帧。

RSV1, RSV2, RSV3（各 1 位）：

    保留位，通常为 0，除非协商了扩展协议。

Opcode（4 位）：定义帧的类型：

    0x0：延续帧（用于分片消息）
    0x1：文本帧（UTF-8 编码）
    0x2：二进制帧
    0x8：连接关闭帧
    0x9：Ping 帧
    0xA：Pong 帧

Mask（1 位）：
    
    指示是否对数据进行掩码处理。

客户端发送的数据帧必须进行掩码处理（Mask 位为 1）。

    服务器发送的数据帧不应进行掩码处理（Mask 位为 0）。

Payload length（7 位或更多）：表示有效载荷的长度：

    0–125：表示有效载荷的字节数。
    126：后续 2 字节表示有效载荷长度（16 位无符号整数）。
    127：后续 8 字节表示有效载荷长度（64 位无符号整数）。

Masking-key（0 或 4 字节）：

    如果 Mask 位为 1，则包含 4 字节的掩码密钥，用于对有效载荷数据进行掩码处理。

Payload Data（x 字节）：

    实际传输的数据，长度由 Payload length 指定。


掩码处理（Masking）

    客户端发送的所有数据帧必须进行掩码处理，以防止代理缓存和其他中间设备的干扰。掩码处理使用 Masking-key 对 Payload Data 进行异或（XOR）操作。服务器接收到掩码处理的数据帧后，使用相同的 Masking-key 对 Payload Data 进行解码

实例:
一下是一个客户端发送的文本消息 "Hello"的数据帧实例(已经惊醒过掩码处理):
```
0x81 0x85 0x37 0xfa 0x21 0x3d 0x7f 0x9f 0x4d 0x51 0x58
```
解释：

    0x81：FIN=1，Opcode=0x1（文本帧）
    0x85：Mask=1，Payload length=5
    0x37 0xfa 0x21 0x3d：Masking-key
    0x7f 0x9f 0x4d 0x51 0x58：掩码处理后的 Payload Data

服务器接收到该帧以后,使用Masking-key对Payload Data进行解码, 回复出原始小时 Hello

## Library and Framework

1. JavaScript /Node.js
    Socket.IO：一个功能丰富的库，提供了自动重连、广播、命名空间、房间等高级功能。它在 WebSocket 不可用时会自动回退到其他传输方式，如 HTTP 长轮询。

    ws：一个轻量级且高性能的 WebSocket 实现，遵循 RFC 6455 标准，适用于需要精细控制的场景。

    SockJS：提供了类似 WebSocket 的 API，并在不支持 WebSocket 的环境中自动回退到其他传输方式，确保兼容性。

2. Python

    websockets：基于 asyncio 的库，专注于简洁性和性能，适合构建高并发的 WebSocket 服务。
    websocket-client：一个适用于 Python 的 WebSocket 客户端库，支持同步和异步操作，易于集成。

3. Java

    Java-WebSocket：一个纯 Java 实现的 WebSocket 客户端和服务器库，适用于桌面和 Android 应用。
    Tyrus：Java EE 的官方 WebSocket 实现，支持注解驱动的开发方式，适合企业级应用。
