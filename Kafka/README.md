# Kafka

What is Kafka?

Kafka is a data transfer platform for different platform. It manager different producers and consumers in itself. And provide the way to producers to send message and producers to fetch data from that platform.

It can bring low dependency for different platforms. and It can transfer data for two different system efficiency and safety. and It always make a chain of event for the whole system. from StepA => StepB => StepC =>.... all the data will be transferred by Kafka, it connected all the different node of the logic let all the logic async and un-dependency

Kafka will store all the data it transferred. That's means it's not like other message queue that the data will missing while the message passed. You can search data you transferred from Kafka database.

## Topic

Topic is a group partitions. That means we can use topic to divide messages with type, and we can send event to one topic, this topic will choose different Partition to send request. Topic is an logic concept. It only appear in the code logic.

## Partition

One topic will have different partition. And each partition only can response for one Topic. And multi Partition can provide the one topic.

## Producer

Data Generate, while the producer generate the data, it should provide the topic, such as:

```json
{
  "key": "user123",  // 可选
  "value": "{ \"userId\": \"user123\", \"action\": \"login\", \"timestamp\": \"2025-05-25T10:00:00Z\" }",
  "timestamp": "2025-05-25T10:00:00Z",
  "headers": {
    "source": "web",
    "version": "1.0"
  }
}
```

```py
# 发送消息 10个消息, topic 是my_topic
for i in range(10):
    message = f"Message {i}"
    producer.produce('my_topic', message.encode('utf-8'), callback=delivery_report)
    producer.poll(0)  # 调用 poll 来处理回调

# 等待所有消息发送完毕
producer.flush()
```

key will choose which partitions this event can enter. that's means the "key" is the topic.
value is value
timestamp: timestamp
headers is an meta data for this event, you can define by your self, and detail info you can see the manual for Kafka

## Consumer

Date receiver, while the consumer fetch the data it should provide the topic. 

```py
# 创建一个 Consumer 实例
consumer = Consumer(conf)

# 订阅主题
consumer.subscribe(['my_topic'])

# 消费消息
try:
    while True:
        msg = consumer.poll(1.0)  # 等待消息，超时为 1 秒

        if msg is None:
            # 没有消息可消费
            continue
        elif msg.error():
            # 错误处理
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print(f"End of partition reached {msg.topic()} [{msg.partition()}] @ {msg.offset()}")
            else:
                raise KafkaException(msg.error())
        else:
            # 正常接收到消息
            print(f"Consumed message: {msg.value().decode('utf-8')}")

except KeyboardInterrupt:
    print("Consumer interrupted")

finally:
    # 关闭 Consumer
    consumer.close()
```

## Broker

It's the instance of Kafka. One System always have multi instance Kafka, because all the producer and consumer have a lot of data need to transfer. One Kafka instance can not afford the request for the transfer work. Then we need add more Kafka instance in to our system to afford all the works which need to be deal with. That's what is Broker's meaning.
Each Broker will have different Topic and has multi Partition each server.
Ont topic of multi partition only have one Leader partition. other partition will sync data from the leader partition.

## Events

Each Event always have some format: it will include the Topic Id, Key and Value.
Consumer always fetch the data from topic, because all the data with the same topic id.

```json
{
  "key": "user123",  // 可选
  "value": "{ \"userId\": \"user123\", \"action\": \"login\", \"timestamp\": \"2025-05-25T10:00:00Z\" }",
  "timestamp": "2025-05-25T10:00:00Z",
  "headers": {
    "source": "web",
    "version": "1.0"
  }
}
```

## Zookeeper

Zookeeper is a manager for all different Broker in a Kafka system. It is maintaining a registry of all the active brokers in the cluster.
Zookeeper is also has a leader broker

Zookeeper is tool only manage Kafka cluster. It's a strong tool to manage all kinds of distribute system.

1. Distribute system config management: distribute system such like HDFS, HBase.
2. Service discovery: Zookeeper maintenance service registry. while server start and register to Zookeeper, other service will discover it and use it
3. Distribute lock: Maintenance share resource for multi client. such as: database, cache etc.
4. Leader Election: node chosen for distribute system. such as Kafka Broker, Hadoop NameNode
5. Name Service: Provide name service such like DNS for distribute system. Let difference server visit each other using name
6. Queue: provide distribute Queue, Task management
7. Status Management: management the status of each node such like: online, offline, suspended etc.

    * Hadoop/HDFS
    * HBase
    * Storm
    * SolrCloud
    * ElasticSearch

# 把我理解的先写出来

1. Partition分为主从, 每个Partition之间的数据都会保持同步
2. 同步数据的时候会有延迟,可能这些Partition处在拨通Broker上,同步是需要时间的, 这样就有可能某些Partition的数据还未完全从Leader上同步过来,这个时候,轮询的时候是不会出现在列表中的.只有当数据同步完成以后,这个Partition处于ISR状态才会负责对外提供服务.
3. 如何避免Consumer 访问到未同步的Replica, 这有两种方法:
    * 配置文件中acks=all, 这样可以实现第二点所说的情况
    * 配置文件中min.insync.replica 这个配置确保在写入数据时候,至少有min.insync.replica 个副本同步完成之才能返回确认,否则就会是写入失败, 从而避免读不到一致的数据.
4. 一个Partition只能负责一个topic的传输, 并且在集群环境中必须只能有一个Partition是Leader.
