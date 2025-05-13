# 服务器端工程师所需要掌握的知识
这是一份全面的 服务器端程序员（后端工程师） 应该掌握的知识体系，涵盖从基础到高级的各个维度。适用于游戏服务器、Web 后端、高并发系统等方向。
## 🔧 一、编程语言 & 工具链
### 必备语言
Go / Rust / C#  熟练掌握至少一门语言的语法、标准库、并发模型、性能优化
### 工具链
构建工具（如 Go Modules、Gradle）
调试工具（delve, pprof, perf）
静态分析 / Lint 工具
单元测试框架 / Mock 工具
## 🧠 二、计算机基础
### 数据结构与算法
实战：倒排索引、Top-K、布隆过滤器等
### 操作系统
内存管理、网络IO模型（epoll/kqueue）
系统调用、上下文切换、调度算法
零拷贝、缓存一致性、Page Cache
### 计算机网络
QUIC / WebSocket
TCP 四次挥手、Nagle、拥塞控制
负载均衡、Keep-Alive、长连接
## 🏗️ 三、后端核心知识
### 网络通信
gRPC、WebSocket、GraphQL
跨语言通信（如 Protobuf）
### 数据库
非关系型：Redis / MongoDB / Cassandra
数据库设计范式、分库分表、中间件（Sharding-JDBC、TiDB）
### 缓存系统
Redis 高级用法：ZSet、Bitmap、HyperLogLog、Lua 脚本、Pipeline
缓存一致性：Cache Aside / Write Through / Write Back
缓存击穿、雪崩、穿透
### 消息队列
RabbitMQ / NATS / Redis Stream
异步处理、削峰填谷、消息重试、顺序性保障
### 存储系统
对象存储（如 MinIO）
KV 存储（RocksDB、LevelDB）
### 安全与认证
TLS / JWT 
数据脱敏、审计日志
## ⚙️ 四、高性能与分布式
### 并发与异步编程
Go 协程模型、Rust 的 async/await
CAS
### 高并发设计
连接管理、线程模型、负载均衡
限流（令牌桶、漏桶）、熔断、降级
### 分布式系统基础
CAP 定理、Paxos / Raft / Gossip 协议
分布式事务（2PC、SAGA、TCC）
一致性哈希、Zookeeper / Etcd、服务注册与发现
### 分布式架构实践
服务拆分、网关（API Gateway）、Sidecar 模式（如 Istio）
负载均衡器：Nginx / Envoy / HAProxy
## 📊 五、监控与运维
### 日志系统
日志收集：ELK、Loki
日志格式：结构化、追踪 ID
### 性能监控
Prometheus + Grafana、OpenTelemetry、Jaeger（链路追踪）
Metrics（QPS、RT、GC、内存占用）
### 运维自动化
Compose、Kubernetes（K8s）
CI/CD：GitHub Actions、ArgoCD
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
CQRS / Event Sourcing
Clean Architecture、Hexagonal Architecture
### 编码实践
SOLID 原则
中间件抽象、模块化设计、接口驱动
## 🎮（可选）游戏服务器开发特别补充
空间划分（Grid、Quadtree）
实时同步（状态同步 / 命令同步）
帧同步、tick-rate 设计
数据驱动设计
帧处理器设计

