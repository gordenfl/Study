# Distribute System

## Basic principle

CAP principle. What is the CAP:

C: Consistency (一致性)
A: Availability (可用性)
P: Partition Tolerance (分区容忍性)

PACELC principle: (这个更加实用,就是在系统处在没有机器坏死的情况下,可用延迟数据还是不可用延迟数据)
PACELC is an extension of CAP. It include 3 concept more：

P：Partition Tolerance（分区容错）
A：Availability（可用性）
C：Consistency（一致性）

E：Else（网络是否分区了, 代表网络中是否有节点中连不上,形成独立的个体了）这里的Else 就代表的时候永远不会有分区坏掉的问题出现, 这个时候只会出现Latency 和 Consistency,就是确保在有delay的情况下数据会保持一致. Fuck!!!
L：Latency（延迟）
C: Consistency(一致性)

后面增加的E, L, C 就是在所有机器都正常的情况下, 你用有延迟的数据,还是你必须要用同步后的数据.


| 网络状态              | 选择权衡       | 缩写组合     | 说明                 | 典型系统举例                |
| ----------------- | ---------- | -------- | ------------------ | --------------------- |
| **Partition (P)** | 一致性 vs 可用性 | PC       | 分区发生时(有机器连不上了)，牺牲可用性保证强一致性  | Google Spanner, HBase |
|                   |            | PA       | 分区发生时(有机器连不上了)，牺牲一致性保证高可用性  | Cassandra, DynamoDB   |
| **Else (E)**      | 一致性 vs 延迟  | EC / E→C | 无分区时(所有的机器都连得上)，选择强一致性，可能延迟较高 | Google Spanner        |
|                   |            | EL / E→L | 无分区时(所有的机器都连得上)，牺牲一致性换取更低延迟   | Cassandra, DynamoDB   |


## Relationship Each other

1. CP: keep the data consistency but can not keep the Availability, that means we can keep all the data fetch from this system are all the same at the same time. but we can not ensure all the request of fetch data is success. That means some database which has not synced the data, it will not provide the service outside

2. AP: Keep the system are all availability, but we can not the data you fetched is the latest version, maybe you got the older data, because that you which you fetch data has not finished the data sync.

3. All the CP and AP can not achieve at the same time in any distribution database(system)

## Core Components:

1. Loadbalance