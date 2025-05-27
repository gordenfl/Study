# TCP Connection and Disconnection 

## TCP Connection Process

It was called Three-way handshake. It always from client to server.

```txt
     CLIENT                        SERVER
----------------------------------------------
     CLOSED                        LISTEN
       |       SYN=1, seq=x           |
       |----------------------------->|
     SYNC_SENT                     LISTEN
       |                              |
       |  SYN=1, ACK=1, seq=y ack=x+1 |
       |<-----------------------------|
     ESTABLISHED                  SYNC_RCVD
       |     ACK=1, seq=x+1 ack=y+1   |
       |----------------------------->|
       |                          ESTABLISHED



```

## TCP Disconnection Process

It was called TCP four times wave!

There are two situation of the TCP connection disconnection:

* Client disconnection actively
* Server break connection actively

```txt
       ACTIVE                      PASSIVE
-------------------------------------------------------
    ESTABLISHED                  ESTABLISHED
         |       FIN=1 seq=x          |
         |--------------------------->| # I do not have data need to send
    FIN_WAIT_1                   ESTABLISHED
         |       ACK=1 ack=x+1        |
         |<---------------------------| # I know you will close the connection
    FIN_WAIT_2                   CLOSE_WAIT
         |       FIN=1 seq=y          |
         |<---------------------------| # I do not have data to send as well
     TIME_WAIT                    LAST_ACK
         |       ACK=1 ack=y+1        |
         |--------------------------->| # I know you will close as well
      CLOSED                        CLOSED
         |         ==== / ====        |
     
```
