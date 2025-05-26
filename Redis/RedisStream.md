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


Redis Stream base Structure:

```mathematica
 Redis Stream: mystream
 ┌─────────────────────────────────────────────────────────────────────┐
 │                     Radix Tree  Prefix Tree                         │
 │ ┌────────────────────────────────────────────────────────────────┐  │
 │ │ Key: 1685065263341-0                                           │  │
 │ │ Value: Listpack -> [ "sensor_id":"123", "temperature":"36.7" ] │  │
 │ └────────────────────────────────────────────────────────────────┘  │
 │ ┌────────────────────────────────────────────────────────────────┐  │
 │ │ Key: 1685065263342-0                                           │  │
 │ │ Value: Listpack -> [ "sensor_id":"124", "temperature":"36.8" ] │  │
 │ └────────────────────────────────────────────────────────────────┘  │
 │ ...                                                                 │
 └─────────────────────────────────────────────────────────────────────┘

 ┌─────────────────────────────┐
 │  Consumer Group: mygroup    │
 │  ┌───────────────────────┐  │
 │  │ last_delivered_id:    │  │
 │  │ 1685065263341-0       │  │
 │  └───────────────────────┘  │
 │  ┌───────────────────────┐  │
 │  │ pending_entries: {...}│  │
 │  └───────────────────────┘  │
 └─────────────────────────────┘
```

Simplify Implement of Redis Stream:

```py
class StreamEntry:
    def __init__(self, entry_id, fields):
        self.entry_id = entry_id  # 唯一ID
        self.fields = fields      # 字段和值（字典）

class RadixTreeNode:
    def __init__(self):
        self.children = {}
        self.entries = {}

class RedisStream:
    def __init__(self):
        self.radix_tree = RadixTreeNode()
        self.last_sequence = 0

    def generate_id(self):
        from time import time
        ms_time = int(time() * 1000)
        self.last_sequence += 1
        return f"{ms_time}-{self.last_sequence}"

    def xadd(self, fields):
        entry_id = self.generate_id()
        entry = StreamEntry(entry_id, fields)
        # 简化为字典存储（实际 Redis 用 Radix Tree + Listpack）
        self.radix_tree.entries[entry_id] = entry
        return entry_id

    def xrange(self, start='-', end='+'):
        entries = sorted(self.radix_tree.entries.items())
        for entry_id, entry in entries:
            print(f"{entry_id}: {entry.fields}")

# 示例
stream = RedisStream()
stream.xadd({"sensor_id": "123", "temperature": "36.7"})
stream.xadd({"sensor_id": "124", "temperature": "36.8"})
stream.xrange()
```