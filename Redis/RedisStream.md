# Redis Stream

What is Redis stream? 
From Redis 5.0, Redis Stream is a important feature of Redis. Redis Stream can deal with Log, MessageQueue, Time series these case.

It is essentially an appendable log structure. Every record has an identical ID and key-value pair.

A Stream:

* FIFO (first in first out) message storage
* A mode support multi consumers like Kafka
* Identical ID for each message like offset of Bitmap
* support Block read, Consumer group, auto-feedback, message resend etc.

Redis Stream is a new type of data

* It can be save through the RDB/AOF way.
* It suit for the Event stream and Log aggregation under distribute system.
* inner consumer groups is an extendable message queue. Easy to use.

Example:
```shell
# 添加一条记录到 stream "mystream"
XADD mystream * sensor_id 123 temperature 36.7

# 读取新记录
XRANGE mystream - +

# 创建消费者组
XGROUP CREATE mystream mygroup $

# 消费者读取记录
XREADGROUP GROUP mygroup consumer1 COUNT 10 STREAMS mystream >

```

Application Scenarios of Redis Stream

* Log System (replace ELK)
* Message Queue (replace RabbitMQ, Kafka)
* Data storage with time order
* Deal with realtime data (Monitoring and alarm)
