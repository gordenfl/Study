# 服务器端工程师所需要掌握的知识
这是一份全面的 服务器端程序员（后端工程师） 应该掌握的知识体系，涵盖从基础到高级的各个维度。适用于游戏服务器、Web 后端、高并发系统等方向。
## 🔧 一、编程语言 & 工具链
### 必备语言
Go / Rust / Java / Python / C# / Node.js（根据业务栈选择）
熟练掌握至少一门语言的语法、标准库、并发模型、性能优化
### 工具链
构建工具（如 Make、Go Modules、Gradle、CMake）
调试工具（gdb, delve, pprof, perf）
静态分析 / Lint 工具
单元测试框架 / Mock 工具
## 🧠 二、计算机基础
### 数据结构与算法
常见结构：数组、链表、栈、队列、哈希表、跳表、堆、树、图
算法：排序、搜索、动态规划、图论、贪心等
实战：LRU、倒排索引、Top-K、布隆过滤器等
### 操作系统
进程 vs 线程、内存管理、文件系统、网络IO模型（epoll/kqueue）
系统调用、上下文切换、死锁、调度算法
mmap、零拷贝、缓存一致性、Page Cache
### 计算机网络
TCP / UDP / QUIC / HTTP/HTTPS / WebSocket
TCP 三次握手、四次挥手、Nagle、拥塞控制
DNS、CDN、负载均衡、Keep-Alive、长连接
Socket 编程、连接池、协议封装（如 Protobuf）
## 🏗️ 三、后端核心知识
### 网络通信
RESTful API 设计、gRPC、WebSocket、GraphQL
多协议支持（TCP/UDP/HTTP）、跨语言通信（如 Protobuf）
### 数据库
关系型：MySQL / PostgreSQL（事务、索引、查询优化、锁机制）
非关系型：Redis / MongoDB / Cassandra
数据库设计范式、分库分表、中间件（Sharding-JDBC、TiDB）
### 缓存系统
Redis 高级用法：ZSet、Bitmap、HyperLogLog、Lua 脚本、Pipeline
缓存一致性：Cache Aside / Write Through / Write Back
缓存击穿、雪崩、穿透
### 消息队列
Kafka / RabbitMQ / NATS / Redis Stream
异步处理、削峰填谷、消息重试、顺序性保障
### 存储系统
对象存储（如 MinIO、S3）
文件系统、块存储、KV 存储（RocksDB、LevelDB）
### 安全与认证
HTTPS / TLS / JWT / OAuth2 / 加解密
数据脱敏、权限控制、审计日志
## ⚙️ 四、高性能与分布式
### 并发与异步编程
Go 协程模型、Java 线程池、Rust 的 async/await
锁机制、CAS、自旋锁、读写锁、信号量
### 高并发设计
连接管理、线程模型、负载均衡
限流（令牌桶、漏桶）、熔断、降级
### 分布式系统基础
CAP 定理、Paxos / Raft / Gossip 协议
分布式事务（2PC、SAGA、TCC）
一致性哈希、Zookeeper / Etcd、服务注册与发现
### 分布式架构实践
微服务 vs 单体架构
服务拆分、网关（API Gateway）、Sidecar 模式（如 Istio）
负载均衡器：Nginx / Envoy / HAProxy
## 📊 五、监控与运维
### 日志系统
日志收集：ELK、Loki
日志格式：结构化、JSON、追踪 ID
### 性能监控
Prometheus + Grafana、OpenTelemetry、Jaeger（链路追踪）
Metrics（QPS、RT、GC、内存占用）
### 运维自动化
Docker、Compose、Kubernetes（K8s）
CI/CD：Jenkins、GitHub Actions、ArgoCD

## 📦 六、部署与工程实践
### 版本控制
Git 流程（GitFlow、 trunk-based）
多分支开发、Tag/Release 管理
### 容器化与部署
镜像构建、配置管理、环境隔离
DevOps 流程与自动化测试/部署
### 可观测性设计
健康检查、熔断机制、慢请求跟踪、报警规则
## 🧩 七、业务建模与设计模式
### 架构模式
DDD（领域驱动设计）
CQRS / Event Sourcing
Clean Architecture、Hexagonal Architecture
### 编码实践
SOLID 原则、设计模式（工厂、策略、观察者等）
中间件抽象、模块化设计、接口驱动
## 🎮（可选）游戏服务器开发特别补充
AOI 系统、空间划分（Grid、Quadtree）
实时同步（状态同步 / 命令同步）
UDP 通信、帧同步、tick-rate 设计
脚本系统（Lua、Python）、数据驱动设计
场景管理、状态机、帧处理器设计