# Quick 

Quick : let use Q to replace that. Q is a protocol and library published with Google, which can make all the Network stream send by UDP can be ordered. And It is very high efficient. We know that the Q is based on C++. It include the Encryption and stream control and multiplexing(多路复用)

## Encrypting and Security

Q using TLS 1.3 protocol. keep all the data safe during transmission

## Connection Rapidly

Q combined encrypting and connection, reduce the handshake in TCP, can build the 0-RTT or 1-RTT connection, reduce the lag. Later I will explain to you about what are 0-RTT and 1-RTT.

### 1-RTT connection (first connection)

1. Client send Initial package: it's include the encryption ClientHello Msg
2. Server give the response for that package: it's include the ServerHello with Encryption and Certification
3. Client confirm: Client send the Finished message with encrypted. after that all the handshake are finished.

### 0-RTT connection (re-connection)

1. Client cached info: TLS Session ticket is cached in client.
2. All the connection using the session ticket before in new connection.
3. Server accept the ticket and accept the connection.

## Multiplexing and non-blocking

Transfer multi-stream in one stream. Avoid the block of TCP while the package loss.

## Connection migration 连接迁移

Q just using uniq ID for each connection, not depend IP address. The connection can transfer to difference device without any delay and reconnection. the session will not break.

## Block Control and Error recovery

Q implement the new block controller algorithm. and error recovery policy. promote the efficiency in the unstable network env.

## Q implemented

* Web Browser of Chrome, Firefox, Safari, and Edge
* HTTP/3 has already based on Q. HTTP/2 based on TCP, Q will be more efficient then HTTP/2
* DNS-over-QUICK: Q is used for DNS query, with encryption of Q, the query becomes more safe.
* Mobile network optimize, because the Connection not depend on IP, it's belong's to ID, apps on different device can make transfer with the same Q connection ID as one connection.

## Example: sync http3 [code](./Example/simple_http3_client.py)

## Example: async http3 [code](./Example/simple_http3_client.py)

```sh
pip install aioquic
```

this quick lib is bases on asyncio.

## Compare with TCP:

| Feature     | TCP            | QUIC          |
| ------ | -------------- | ------------- |
| Protocol Type   | Based on Connection reliable protocol  | Reliable Protocol based on UDP |
| Multiplexing   | Support HTTP/2 layer   | Multiplexing support        |
| Connection Time-Consuming | at least 1-RTT + TLS | faster 0-RTT can transfer data |
| Encrypt     | Based on TLS layer       | Build in TLS 1.3    |
| Connection Migration  | not support            | support |
| Deploy flexibility  | May blocked by firewall | easy to go through firewall     |

## Quick Package Construction

Two part of each package:

```sh
| UDP Header | QUIC Header | Encrypted Payload (Frame) |
```

1. QUICK Header: include version, connection ID, package number etc.
2. Frame: data frame, control frame, ACK frame etc. you can extend it.
3. UDP Header is basic layer package info, it include the source port, destination port, length, checksum.

一个QUICK 连接的 CID是与这个设备的地址,连接状态,加密身份验证信息,包序列绑定的.是复发在另个设备上同时当一个设备连上服务器的.
只有这个设备当前的网络切换才可以,可以通过0-RTT来重连上去.

