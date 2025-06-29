# System Design Common knowledge

## Key Concept

1. PACELC theorem 这个理论在 [Distribute System](../Distribute%20System/README.md)
2. Hearbeat
3. AJAX polling (就是用Ajax 定时访问接口,有数据就返回, 没有数据就返回空)
4. HTTP Long-polling (就是用HTTP request, 如果有数据就返回,没有数据就挂起来等有数据再返回)
5. Websockets: 服务器,客户端双向交流数据
6. Server-sent events (SSEs):客户端服务器端建立TCP连接,不断,双方通信

7. 基本的分布式系统

    * 数据持久性和一致性
    * Replication 副本: 完全复制
    * Partitioning 分区 : 每个区装不同的数据
    * Consensus 共识: 确认每个节点的数据都能够保持一致
    * Distributed Transactions

8. 大型Web系统的分布式架构

    * N-tier Applications : 分层, 显示层, 逻辑层, basic 层, 数据层, 这些东西分布在不同的服务器上
    * HTTP 和 REST, REST就是 GET:获取, POST:增加, PUT:修改, DELETE:删除
    * DNS and loadbalance: DNS 是平均的, loadbalance是可以随着服务器不同负载进行调整的
    * Caching: 缓存, 需要考虑的是哪些数据放缓存,哪些放数据库,缓存过期加锁, 去取新数据,否则会让数据库崩溃这个叫做 "缓存雪崩 Cache Avalanche"
    * Steam processing: 流处理, 一般对于长时间会持续数据传递的过程, 比如: log, 监控, 实时推荐, 音视频, 数据实时分析,一般来说可以用Kafka, rabbitMQ, Flink SparkStreaming 等等

9. 设计大型的分布式系统
