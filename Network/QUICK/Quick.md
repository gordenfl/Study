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
